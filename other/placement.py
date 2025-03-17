import enum


class Placement(enum.Enum):
    BEFORE = DEFAULT = enum.auto()
    PREFIX = enum.auto()
    SUFFIX = enum.auto()
    DISABLED = enum.auto()
