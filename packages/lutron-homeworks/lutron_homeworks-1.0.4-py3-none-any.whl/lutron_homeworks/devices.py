import abc
import asyncio
import logging
import re
import typing

import attr

from lutron_homeworks.events import Dispatcher, HomeworksEvent
from lutron_homeworks.message import HomeworksMessage, normalize_address

logger = logging.getLogger("lutron_homeworks").getChild(__name__)

if typing.TYPE_CHECKING:
    from lutron_homeworks.client import HomeworksClient

address_splitter = re.compile(r'[.:\/]')
address_re = re.compile(r'^\[?(?:[0-9]{1,2}[.:\/]){2,4}[0-9]{1,2}\]?$')


@attr.s
class Device(abc.ABC):
    TYPE = "unknown"
    HANDLES_ACTIONS = []

    class Event(HomeworksEvent):
        CHANGED = 1

    _client: "HomeworksClient" = attr.ib()
    address: str = attr.ib(converter=normalize_address)
    events: Dispatcher = attr.ib(factory=Dispatcher)

    def event_dispatch(self, event: HomeworksEvent, params: dict):
        params.update({"device": self})
        self.events.dispatch(event, params)

    @address.validator
    def check_address(self, attribute, value):
        if not address_re.match(value):
            raise ValueError("Address is wrong")

    @abc.abstractmethod
    def handle(self, message: HomeworksMessage) -> None:
        pass


class Dimmer(Device):
    TYPE = "dimmer"
    HANDLES_ACTIONS = ['DL']
    intensity: int = 0

    def handle(self, message: HomeworksMessage) -> None:
        if message.action == "DL":
            self.intensity = int(message.vars[0])
            self.event_dispatch(self.Event.CHANGED, {
                "new_intensity": self.intensity
            })

    async def fade(self, intensity: int, fade_time: int = 0, delay_time: int = 0):
        assert 0 <= intensity <= 100
        assert 0 <= fade_time <= 60
        assert 0 <= delay_time <= 60
        self._client.send_command('FADEDIM, %d, %d, %d, %s' % (intensity, fade_time, delay_time, self.address))

    async def flash(self, intensity: int, flash_rate: int = 0):
        assert 0 <= intensity <= 100
        assert 0 <= flash_rate <= 60
        self._client.send_command('FLASHDIM, %d, %d, %s' % (intensity, flash_rate, self.address))

    async def stop_flash(self):
        self._client.send_command('STOPFLASH, %s' % (self.address))

    async def raise_brightness(self):
        self._client.send_command('RAISEDIM, %s' % (self.address))

    async def lower_brightness(self):
        self._client.send_command('LOWERDIM, %s' % (self.address))

    async def stop_brightness_change(self):
        self._client.send_command('STOPDIM, %s' % (self.address))

    async def request_level(self):
        self._client.send_command('RDL, %s' % (self.address))

    @classmethod
    async def discover(cls, client: "HomeworksClient", params: dict = None):
        elements = cls._get_discover_params(params)

        for processor in elements['processors']:
            for link in elements['links']:
                for router in elements['routers']:
                    for module in elements['modules']:
                        for output in range(1,5):
                            address = '[%02d:%02d:%02d:%02d:%02d]' % (processor, link, router, module, output)
                            await cls(client, address).request_level()
                            await asyncio.sleep(0.05)

    @classmethod
    def _get_discover_params(cls, params):
        elements = {
            'processors': [1],
            'links':      [1],
            'routers':    [0],
            'modules':    range(1, 9),
            'outputs':    range(1, 5),
        }
        if params is not None:
            assert isinstance(params, dict)
            assert all((isinstance(v, (range, list)) for (k, v) in params.items()))
            elements.update(params)
        return elements


class ButtonControl(Device):
    class Event(HomeworksEvent):
        BUTTON_PRESS = 1
        BUTTON_RELEASE = 2
        BUTTON_HOLD = 3
        BUTTON_DOUBLE_TAP = 4
        CHANGED = 5
        LED_CHANGED = 6

    def handle(self, message: HomeworksMessage) -> None:
        if message.action not in self.HANDLES_ACTIONS:
            return

        params = {
            "button_nr": int(message.vars[0])
        }
        if message.action.endswith("P"):
            self.event_dispatch(self.Event.BUTTON_PRESS, params)
        elif message.action.endswith("R"):
            self.event_dispatch(self.Event.BUTTON_RELEASE, params)
        elif message.action.endswith("H"):
            self.event_dispatch(self.Event.BUTTON_HOLD, params)
        elif message.action.endswith("DT"):
            self.event_dispatch(self.Event.BUTTON_DOUBLE_TAP, params)

    async def button_tap(self, button_nr):
        await self.button_press(button_nr)
        await asyncio.sleep(0.1)
        await self.button_release(button_nr)

    @abc.abstractmethod
    async def button_press(self, button_nr: int):
        pass

    @abc.abstractmethod
    async def button_release(self, button_nr: int):
        pass

    @abc.abstractmethod
    async def button_hold(self, button_nr: int):
        pass

    @abc.abstractmethod
    async def button_double_tap(self, button_nr: int):
        pass


class KeypadControl(ButtonControl):
    TYPE = "keypad"
    HANDLES_ACTIONS = ["KBP", "KBR", "KBH", "KBDT", "KES", "KLS"]
    enabled: bool = True

    def handle(self, message: HomeworksMessage) -> None:
        super().handle(message)

        if message.action == "KES":
            self.enabled = message.vars[0] == "enabled"
            self.event_dispatch(self.Event.CHANGED, {
                "enabled": self.enabled
            })
        elif message.action == "KLS":
            self.event_dispatch(self.Event.LED_CHANGED, {
                "led_state": message.vars[0]  # TODO: parse according to manual
            })

    async def button_press(self, button_nr: int):
        self._client.send_command('KBP, %s, %d' % (self.address, button_nr))

    async def button_release(self, button_nr: int):
        self._client.send_command('KBR, %s, %d' % (self.address, button_nr))

    async def button_hold(self, button_nr: int):
        self._client.send_command('KBH, %s, %d' % (self.address, button_nr))

    async def button_double_tap(self, button_nr: int):
        self._client.send_command('KBDT, %s, %d' % (self.address, button_nr))

    async def enable(self):
        self._client.send_command('KE, %s' % (self.address))
        await self.request_enabled_state()

    async def disable(self):
        self._client.send_command('KD, %s' % (self.address))
        await self.request_enabled_state()

    async def request_enabled_state(self):
        self._client.send_command('RKES, %s' % (self.address))


class DimmerControl(ButtonControl):
    TYPE = "dimmer_control"
    HANDLES_ACTIONS = ["DBP", "DBR", "DBH", "DBDT"]

    async def button_press(self, button_nr: int):
        self._client.send_command('DBP, %s, %d' % (self.address, button_nr))

    async def button_release(self, button_nr: int):
        self._client.send_command('DBR, %s, %d' % (self.address, button_nr))

    async def button_hold(self, button_nr: int):
        self._client.send_command('DBH, %s, %d' % (self.address, button_nr))

    async def button_double_tap(self, button_nr: int):
        self._client.send_command('KBDT, %s, %d' % (self.address, button_nr))


class SivoiaControl(ButtonControl):
    TYPE = "sivoia_control"
    HANDLES_ACTIONS = ["SVBP", "SVBR", "SVBH", "SVBDT"]

    async def button_press(self, button_nr: int):
        self._client.send_command('SVBP, %s, %d' % (self.address, button_nr))

    async def button_release(self, button_nr: int):
        self._client.send_command('SVBR, %s, %d' % (self.address, button_nr))

    async def button_hold(self, button_nr: int):
        self._client.send_command('SVBH, %s, %d' % (self.address, button_nr))

    async def button_double_tap(self, button_nr: int):
        self._client.send_command('SVBDT, %s, %d' % (self.address, button_nr))


class CCORelay(Device):
    def handle(self, message: HomeworksMessage) -> None:
        pass

    TYPE = "cco_relay"
    async def relay_open(self, relay_nr: int):
        self._client.send_command('CCOOPEN, %s, %d' % (self.address, relay_nr))

    async def relay_close(self, relay_nr: int):
        self._client.send_command('CCOCLOSE, %s, %d' % (self.address, relay_nr))

    async def relay_pulse(self, relay_nr: int, pulse_time: float):
        assert 0.5 <= pulse_time <= 122.5
        self._client.send_command('CCOPULSE, %s, %d, %d' % (self.address, relay_nr, pulse_time * 2))
