from enum import Enum

class BlockState(Enum):
    WhiteSquare = 1
    BlackSquare = 2
    BlackTopLeftCornerSquare = 3
    BlackTopRightCornerSquare = 4
    BlackBottomLeftCornerSquare = 5
    BlackBottomRightCornerSquare = 6
    WhiteDiamond = 7
    BlackDiamond = 8
    BlackTopCornerDiamond = 9
    BlackBottomCornerDiamond = 10
