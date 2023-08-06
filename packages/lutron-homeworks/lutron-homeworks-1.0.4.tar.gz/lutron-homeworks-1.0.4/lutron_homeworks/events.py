import logging
from collections import defaultdict
from enum import Enum
from typing import Callable, List, Mapping

logger = logging.getLogger("lutron_homeworks").getChild(__name__)


class HomeworksEvent(Enum):
    pass


_SUBSCRIBER_DEFINITION = Callable[[HomeworksEvent, dict], None]


class Dispatcher:
    def __init__(self):
        self._subscribers: Mapping[HomeworksEvent, List[_SUBSCRIBER_DEFINITION]] = defaultdict(list)

    def subscribe(self, event: HomeworksEvent, fn: _SUBSCRIBER_DEFINITION):
        self._subscribers[event].append(fn)

    def unsubscribe(self, event: HomeworksEvent, fn: _SUBSCRIBER_DEFINITION):
        self._subscribers[event].remove(fn)

    def dispatch(self, event: HomeworksEvent, params: dict):
        for subscriber in self._subscribers[event]:
            try:
                subscriber(event, params)
            except:
                logger.exception("Exception in event handler")