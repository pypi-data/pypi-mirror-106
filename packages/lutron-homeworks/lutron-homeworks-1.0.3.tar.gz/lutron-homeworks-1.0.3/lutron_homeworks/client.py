import asyncio
import logging
import math
from abc import ABC, abstractmethod
from asyncio.transports import Transport
from enum import IntEnum
from time import time
from typing import Type, Mapping, Set

from .devices import Device
from .events import HomeworksEvent, Dispatcher
from .exceptions import HomeworksAuthenticationException, HomeworksConnectionLost
from .message import HomeworksMessage, normalize_address

try:
    import serial_asyncio
except ImportError:
    serial_asyncio = None

from .protocol import HomeworksProtocol


logger = logging.getLogger("lutron_homeworks").getChild(__name__)


class RunState(IntEnum):
    START = 0
    CONNECTING = 1
    CONNECTED = 2
    READY = 3
    CONNECTION_LOST = 4
    STOPPED = 5


class HomeworksClient(ABC):
    _transport: Transport = None
    _protocol: HomeworksProtocol = None
    _loop_future: asyncio.Future = None
    _read_queue_worker: asyncio.Future = None
    _state: RunState = RunState.START
    events: Dispatcher
    _device_types: Set[Type[Device]]
    _device_registry: Mapping[str, Device]

    MAX_RECONNECT_TIME = 10.0 # seconds

    class Event(HomeworksEvent):
        STATE_CHANGE = "state_change"
        MESSAGE = "message"
        NEW_DEVICE = "new_device"

    def __init__(self):
        super(HomeworksClient, self).__init__()
        self._device_registry = {}
        self._device_types = set()

        self.events = Dispatcher()

    @property
    def state(self) -> RunState:
        return self._state

    def _set_state(self, state: RunState):
        old_state = self._state
        if old_state != state and self._state != RunState.STOPPED:
            self._state = state
            self.events.dispatch(self.Event.STATE_CHANGE, {
                "new_state": self._state,
                "old_state": old_state,
                "client": self
            })

    def start(self):
        self._loop_future = asyncio.ensure_future(self.loop())

    def stop(self):
        self._set_state(RunState.STOPPED)
        if self._transport:
            self._transport.close()

    @abstractmethod
    async def connect(self):
        pass

    async def configure_connection(self):
        await self._protocol.wait_ready()  # Do not send any messages until protocol will be ready
        self._set_state(RunState.CONNECTED)

        self._protocol.writeln('PROMPTOFF')  # No prompt is needed
        self._protocol.writeln('KBMON')  # Monitor keypad events
        self._protocol.writeln('GSMON')  # Monitor GRAFIKEYE scenes
        self._protocol.writeln('DLMON')  # Monitor dimmer levels
        self._protocol.writeln('KLMON')  # Monitor keypad LED states

        self._set_state(RunState.READY)

    def send_command(self, command: str) -> None:
        self._protocol.writeln(command)

    async def loop(self):
        fast_closed_connection_count = 0
        while True:
            start_time = time()

            try:
                logger.info("Connecting")
                self._set_state(RunState.CONNECTING)
                await self.connect()
                self._read_queue_worker = asyncio.ensure_future(self._message_queue_loop())
                await self._protocol.wait_connection_lost()

            except (IOError, HomeworksConnectionLost) as e:
                logger.error(f'Connection error: {e}')
                self._set_state(RunState.CONNECTION_LOST)

            except HomeworksAuthenticationException as e:
                logger.critical("Unable to authenticate. Verify credentials")
                self.stop()
                raise

            finally:
                if self._read_queue_worker:
                    self._read_queue_worker.cancel()
                    self._read_queue_worker = None

                if self.state == RunState.STOPPED:
                    return

                connection_duration = time() - start_time

                if connection_duration < 5:  # Connection closed too fast
                    fast_closed_connection_count += 1
                else:
                    fast_closed_connection_count = 0

                await self._delay_next_connection_attempt(fast_closed_connection_count)

    async def _delay_next_connection_attempt(self, fast_closed_connection_count: int):
        delay = min(self.MAX_RECONNECT_TIME, 0.01 * math.exp(fast_closed_connection_count))
        await asyncio.sleep(delay)

    async def _message_queue_loop(self):
        while True:
            raw = await self._protocol.read_queue.get()
            asyncio.create_task(self.process_message(raw))

    def register_device_type(self, type: Type[Device]):
        self._device_types.add(type)

    async def process_message(self, raw: str):
        logger.debug("Raw: %s", raw)
        message = HomeworksMessage(raw)

        try:
            message.parse()
            if not message.is_parsed:
                logger.warning("Not handling: %s", raw)
                return

            device_class: Type[Device] = filter(lambda candidate: message.action in candidate.HANDLES_ACTIONS, self._device_types).__next__()

            device = self.get_device(message.address)
            if device is None:
                device = self.make_device(message.address, device_class)
                self.register_device(device)

            device.handle(message)

        except StopIteration:
            logger.debug("No handler for message found")
        except:
            logger.exception("Exception during handling: %s", raw)
        finally:
            self.events.dispatch(self.Event.MESSAGE, {
                "message": message,
                "client": self
            })

    def get_device(self, address: str) -> Device:
        return self._device_registry.get(normalize_address(address))

    @property
    def devices(self):
        return self._device_registry.values()

    def register_device(self, device: Device) -> None:
        self.register_device_type(type(device))
        self._device_registry[device.address] = device
        self.events.dispatch(self.Event.NEW_DEVICE, {
            "device": device,
            "client": self
        })

    def make_device(self, address: str, device_class: Type[Device]) -> Device:
        assert device_class is not None
        return device_class(client=self, address=address)


class HomeworksSerialClient(HomeworksClient):
    def __init__(self, port, baudrate=115200, credentials=None):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.credentials = credentials

    async def connect(self):
        if not serial_asyncio:
            raise ImportError("You need to install 'pyserial-asyncio' if you want to use serial connection")

        self._transport, self._protocol = await serial_asyncio.create_serial_connection(
            asyncio.get_event_loop(),
            lambda: HomeworksProtocol(self.credentials),
            self.port,
            baudrate=self.baudrate
        )

        await self.configure_connection()


class HomeworksTelnetClient(HomeworksClient):
    def __init__(self, host, port, credentials=None):
        super().__init__()
        self.host = host
        self.port = port
        self.credentials = credentials

    async def connect(self):
        loop = asyncio.get_event_loop()
        self._transport, self._protocol = await loop.create_connection(
            lambda: HomeworksProtocol(self.credentials),
            host=self.host,
            port=self.port
        )

        await self.configure_connection()

