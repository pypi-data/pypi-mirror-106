import re
import logging
import typing

import attr

argument_splitter = re.compile(r'\s*,\s*')
address_splitter = re.compile(r'[.:\/]')
address_re = re.compile(r'^\[?(?:[0-9]{1,2}[.:\/]){2,4}[0-9]{1,2}\]?$')

logger = logging.getLogger("lutron_homeworks").getChild(__name__)


def find_address(value):
    match = address_re.match(value)
    if not match:
        return None
    return normalize_address(match.group(0))


def normalize_address(value: str):
    parts = address_splitter.split(value.strip("[]"))
    padded_parts = map(lambda x: x.rjust(2,"0"), parts)
    joined = ":".join(padded_parts)
    return f"[{joined}]"


def parse_address(raw_address):
    assert address_re.match(raw_address)
    return normalize_address(raw_address)


@attr.s
class HomeworksMessage:
    raw: str = attr.ib()
    action: str = attr.ib(default=None)
    address: str = attr.ib(default=None)
    vars: typing.List[str] = attr.ib(factory=list)

    is_parsed: bool = attr.ib(default=False)

    def parse(self):
        parts = argument_splitter.split(self.raw)

        try:
            self.action = parts.pop(0)
            self.address = parse_address(parts.pop(0))

            self.vars = parts

            self.is_parsed = True
        except (IndexError, AssertionError):
            self.is_parsed = False
