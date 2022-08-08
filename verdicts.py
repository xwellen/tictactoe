from enum import Enum, auto, unique

@unique
class Verdict(Enum):
    WIN_X = auto()
    WIN_O = auto()
    DRAW = auto()
    NA = auto()