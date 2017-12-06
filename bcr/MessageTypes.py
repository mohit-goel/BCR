from enum import Enum


class MessageTypes(Enum):
    DIRECT = 0
    FORWARDED = 1
    SHUTTLE = 2
    RESULT_SHUTTLE = 3
    CHECKPOINT = 4
    COMPLETED_CHECKPOINT = 5
    WEDGE_REQUEST = 6
    NEW_CONFIGURATION = 7
    GET_RUNNUNG_STATE = 8
    CATCH_UP = 9
