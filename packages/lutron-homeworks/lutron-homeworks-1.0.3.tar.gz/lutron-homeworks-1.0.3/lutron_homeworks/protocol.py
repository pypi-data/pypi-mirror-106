import asyncio
import logging
from asyncio.queues import Queue
from asyncio.transports import Transport
from typing import Optional, Callable, Union

from lutron_homeworks.exceptions import HomeworksNoCredentialsProvided, \
    HomeworksInvalidCredentialsProvided, HomeworksConnectionLost

logger = logging.getLogger("lutron_homeworks").getChild(__name__)

ENCODING = 'ascii'


def ensure_bytes(data: Optional[Union[str, bytes]]):
    if isinstance(data, bytes) or data is None:
        return data

    return data.encode(ENCODING)


class HomeworksProtocol(asyncio.Protocol):
    read_queue: Queue
    _transport: Transport

    LOGIN_PROMPT_WAIT_TIMEOUT = 1.
    PROMPT_REQUESTS = [b'LNET> ', b'L232> ']
    LOGIN_REQUEST = b'LOGIN: '
    COMMAND_SEPARATOR = b'\r\n'

    def __init__(self, credentials: str = None):
        self.ready_future = asyncio.Future()
        self.connection_lost_future = asyncio.Future()

        self.read_queue = Queue()
        self._buffer = b''
        self._transport = None
        self._credentials = credentials

    async def wait_ready(self):
        await self.ready_future

    async def wait_connection_lost(self):
        await self.connection_lost_future

    def data_received(self, data: bytes) -> None:
        logger.debug(f"received: {data}")
        self._buffer += data

        try:
            self.handle_buffer_increment()
        except Exception as e:
            if not self.ready_future.done():
                self.ready_future.set_exception(e)

            if not self.connection_lost_future.done():
                self.connection_lost_future.set_exception(e)

            self._transport.close()

    def connection_made(self, transport: Transport) -> None:
        logger.info("Socket connected")
        self._transport = transport

        self.write('A\b')  # Do not wait for LOGIN: prompt. Ask for it

    def connection_lost(self, exc: Optional[Exception]) -> None:
        logger.error("Connection lost")
        self._transport = None

        if exc is None and self.connection_lost_future.done():
            exception = self.connection_lost_future.exception()
        else:
            exception = HomeworksConnectionLost(f'Connection lost before ready state: {exc}')  # TODO: This fires on normal shut down

        if not self.ready_future.done():
            self.ready_future.set_exception(exception)

        if not self.connection_lost_future.done():
            self.connection_lost_future.set_exception(exception)

    def handle_buffer_increment(self):
        while any([
            self._check_login_prompt(),
            self._trim_prompts(),
            self._check_messages()
        ]):
            pass

    def writeln(self, data: Union[str, bytes]):
        self.write(ensure_bytes(data) + self.COMMAND_SEPARATOR)

    def write(self, data: Union[str, bytes]):
        data = ensure_bytes(data)

        if not self._transport.is_closing():
            logger.debug(f"sending: {data}")
            self._transport.write(data)

    def _check_login_prompt(self) -> bool:
        return self._trim_prefix(self.LOGIN_REQUEST, self._on_login_prompt_found)

    def _trim_prompts(self) -> bool:
        return any(self._trim_prefix(prompt, self._on_prompt_found) for prompt in self.PROMPT_REQUESTS)

    def _on_prompt_found(self, _):
        self._notify_ready()

    def _on_login_prompt_found(self, _):
        if not self._credentials:
            raise HomeworksNoCredentialsProvided()

        self.writeln(self._credentials)

    def _trim_prefix(self, prefix: bytes, on_match: Callable[[bytes], None]) -> bool:
        if self._buffer.startswith(prefix):
            self._buffer = self._buffer[len(prefix):]
            on_match(prefix)
            return True

        return False

    def _check_messages(self) -> bool:
        (command, separator, remainder) = self._buffer.partition(self.COMMAND_SEPARATOR)
        if separator != self.COMMAND_SEPARATOR:
            return False
        self._buffer = remainder

        command = command.strip()
        if command == b'':
            return True

        self._handle_message(command.decode(ENCODING))

        return True

    def _handle_message(self, message: str):
        if message == "login successful":
            logger.info("Authentication succeeded")
            self._notify_ready()
            return
        elif message == "login incorrect":
            logger.error("Authentication failed")
            raise HomeworksInvalidCredentialsProvided()

        self._notify_ready()
        self.read_queue.put_nowait(message)

    def _notify_ready(self):
        if self._transport is not None and not self.ready_future.done():
            self.ready_future.set_result(True)
