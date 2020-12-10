from enum import Enum

'''
Represents the possible orientations of the block.
'''
class BlockOrientation(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

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
    Unknown = 7 # Refers to a forgotten block

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
    PickUpFromBank = 9
    PlaceInPuzzle = 10

class PuzzleAction(Enum):
    LookAtPuzzle = 1

''' Represents the type of search functions for the puzzle. '''
class SearchType(Enum):
    Face = 1 # Given some block, find a face
    PuzzlePiece = 2 # Given some puzzle, find the next puzzle piece to solve
