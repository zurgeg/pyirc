from enum import Enum, auto

class EventTypes(Enum):
    MESSAGE = auto()
    MEMBER_LEAVE = auto()
    MEMBER_JOIN = auto()