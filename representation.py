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

    # Leave out 45 degree rotation
    # problems for now to simplify the model

    # WhiteDiamond = 7
    # BlackDiamond = 8
    # BlackTopCornerDiamond = 9
    # BlackBottomCornerDiamond = 10

''' When a face is rotated 90 degrees. '''
class RotateDirection(Enum):
    Right = 1
    Left = 2

''' When a face is flipped over to another face. '''
class FlipDirection(Enum):
    Up = 1
    Left = 2
    Down = 3
    Right = 4

''' Orientation based on descriptors below. '''
class BlockOrientation(Enum):
    Up = 1
    Left = 2
    Down = 3
    Right = 4

'''
A block has six faces. Each face is assigned a number.

When collapsed to 2D, they look like...
                  
                 BlackTopRightCornerSquare (1)
                             ^
    WhiteSquare (2) | WhiteSquare (3) | BlackSquare (4) | Black Square (5)
                             v
                 BlackBottomRightCornerSquare (6)

By convention, we will say this is the default orientation of 'up', when
1 is above 3.

If the WhiteSquare (3) has BlackSquare (4) oriented upwards, we'll call that
an orientation of 'right', and so on.
'''
class Block:

    def __init__(self, number, orientation):
        this.face = (number, orientation)
        this.patterns = {
            1: {
                BlockOrienation.Up: BlockPattern.BlackTopRightCornerSquare,
                BlockOrienation.Right: BlockPattern.BlackTopLeftCornerSquare,
                BlockOrienation.Bottom: BlockPattern.BlackBottomLeftCornerSquare,
                BlockOrienation.Left: BlockPattern.BlackBottomRightCornerSquare,
            },
            2: {
                BlockOrienation.Up: BlockPattern.WhiteSquare,
                BlockOrienation.Right: BlockPattern.WhiteSquare,
                BlockOrienation.Bottom: BlockPattern.WhiteSquare,
                BlockOrienation.Left: BlockPattern.WhiteSquare,
            },
            3: {
                BlockOrienation.Up: BlockPattern.WhiteSquare,
                BlockOrienation.Right: BlockPattern.WhiteSquare,
                BlockOrienation.Bottom: BlockPattern.WhiteSquare,
                BlockOrienation.Left: BlockPattern.WhiteSquare,
            },
            4: {
                BlockOrienation.Up: BlockPattern.BlackSquare,
                BlockOrienation.Right: BlockPattern.BlackSquare,
                BlockOrienation.Bottom: BlockPattern.BlackSquare,
                BlockOrienation.Left: BlockPattern.BlackSquare,
            },
            5: {
                BlockOrienation.Up: BlockPattern.BlackSquare,
                BlockOrienation.Right: BlockPattern.BlackSquare,
                BlockOrienation.Bottom: BlockPattern.BlackSquare,
                BlockOrienation.Left: BlockPattern.BlackSquare,
            },
            6: {
                BlockOrienation.Up: BlockPattern.BlackBottomRightCornerSquare,
                BlockOrienation.Right: BlockPattern.BlackTopRightCornerSquare,
                BlockOrienation.Bottom: BlockPattern.BlackTopLeftCornerSquare,
                BlockOrienation.Left: BlockPattern.BlackBottomLeftCornerSquare,
            },
        }


    def getPattern():
        return this.patterns[this.face[0]][this.face[1]]
   
    def flipUp():
        pass
        
    def flipDown():
        pass
            
    def flipRight():
        pass
            
    def flipUp():
        pass

    ''' Change orientation, but stay on the same face. '''
    def rotateRight():
        pass
        
    ''' Change orientation, but stay on the same face. '''
    def rotateLeft():
        pass

