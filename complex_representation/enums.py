from enum import Enum

'''
Represents the possible patterns of the block.
'''
class BlockPattern(Enum):
    WhiteSquare = 1
    BlackSquare = 2
    BlackTopLeftCornerSquare = 3
    BlackTopRightCornerSquare = 4
    BlackBottomLeftCornerSquare = 5
    BlackBottomRightCornerSquare = 6

'''
Represents the possible actions for the block.
'''
class BlockAction(Enum):
    GoToFaceOne = 1
    GoToFaceTwo = 2
    GoToFaceThree = 3
    GoToFaceFour = 4
    GoToFaceFive = 5
    GoToFaceSix = 6
    RotateLeft = 7
    RotateRight = 8
