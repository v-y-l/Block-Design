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
    Right = 2
    Down = 3
    Left = 4

''' Orientation based on descriptors below. '''
class BlockOrientation(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

''' For a doubly linked list '''
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

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

    def __init__(self, number=1, orientation=BlockOrientation.Up):
        self.face = (number, orientation)
        self.patterns = {
            1: {
                BlockOrientation.Up: BlockPattern.BlackTopRightCornerSquare,
                BlockOrientation.Right: BlockPattern.BlackTopLeftCornerSquare,
                BlockOrientation.Down: BlockPattern.BlackBottomLeftCornerSquare,
                BlockOrientation.Left: BlockPattern.BlackBottomRightCornerSquare,
            },
            2: {
                BlockOrientation.Up: BlockPattern.WhiteSquare,
                BlockOrientation.Right: BlockPattern.WhiteSquare,
                BlockOrientation.Down: BlockPattern.WhiteSquare,
                BlockOrientation.Left: BlockPattern.WhiteSquare,
            },
            3: {
                BlockOrientation.Up: BlockPattern.WhiteSquare,
                BlockOrientation.Right: BlockPattern.WhiteSquare,
                BlockOrientation.Down: BlockPattern.WhiteSquare,
                BlockOrientation.Left: BlockPattern.WhiteSquare,
            },
            4: {
                BlockOrientation.Up: BlockPattern.BlackSquare,
                BlockOrientation.Right: BlockPattern.BlackSquare,
                BlockOrientation.Down: BlockPattern.BlackSquare,
                BlockOrientation.Left: BlockPattern.BlackSquare,
            },
            5: {
                BlockOrientation.Up: BlockPattern.BlackSquare,
                BlockOrientation.Right: BlockPattern.BlackSquare,
                BlockOrientation.Down: BlockPattern.BlackSquare,
                BlockOrientation.Left: BlockPattern.BlackSquare,
            },
            6: {
                BlockOrientation.Up: BlockPattern.BlackBottomRightCornerSquare,
                BlockOrientation.Right: BlockPattern.BlackTopRightCornerSquare,
                BlockOrientation.Down: BlockPattern.BlackTopLeftCornerSquare,
                BlockOrientation.Left: BlockPattern.BlackBottomLeftCornerSquare,
            },
        }

        up = Node(BlockOrientation.Up)
        right = Node(BlockOrientation.Right)
        down = Node(BlockOrientation.Down)
        left = Node(BlockOrientation.Left)

        up.prev = left
        up.next = right
        right.prev = up
        right.next = down
        down.prev = right
        down.next = left
        left.prev = down
        left.next= up

        self.orientations = {
            BlockOrientation.Up: up,
            BlockOrientation.Right: right,
            BlockOrientation.Down: down,
            BlockOrientation.Left: left,
        }


    def getPattern(self):
        number, orientation = self.face
        return self.patterns[number][orientation]
   
    def flipUp(self):
        pass
        
    def flipDown(self):
        pass
            
    def flipRight(self):
        pass
            
    def flipUp(self):
        pass

    ''' Change orientation, but stay on the same face. '''
    def rotateRight(self):
        number, orientation = self.face
        nextOrientation = self.orientations[orientation].prev.val
        self.face = (number, nextOrientation)
        
    ''' Change orientation, but stay on the same face. '''
    def rotateLeft(self):
        number, orientation = self.face
        nextOrientation = self.orientations[orientation].next.val
        self.face = (number, nextOrientation)


