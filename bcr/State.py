from enum import Enum


class State(Enum):
    PENDING = 0
    IMMUTABLE = 1
    ACTIVE = 2
