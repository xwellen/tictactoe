from enum import Enum, auto, unique


@unique
class TileState(Enum):
    X = auto()
    O = auto()
    EMPTY = auto()
