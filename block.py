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


''' A node to represent a face. '''
class BlockNode:
    
    def __init__(self, number):
        self.val = number
        self.neighbors = {}


'''
A block has six faces. Each face is assigned a number.

When collapsed to 2D, they look like...
                  
 
                 BlackTopRightCornerSquare (1, ^)
                             |
    WhiteSquare (2, ^) | WhiteSquare (3, ^) | BlackSquare (4, ^) | Black Square (5, ^)
                             |
                 BlackBottomRightCornerSquare (6, ^)

By convention, each face has the default orientation of 'up' or ^.
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

        # Returns a node to the doubly linked list that determines
        # the clockwise order starting from up.
        self.orientations = {
            BlockOrientation.Up: up,
            BlockOrientation.Right: right,
            BlockOrientation.Down: down,
            BlockOrientation.Left: left,
        }

        self.opposites = {
            BlockOrientation.Up: BlockOrientation.Down,
            BlockOrientation.Right: BlockOrientation.Left,
            BlockOrientation.Down: BlockOrientation.Up,
            BlockOrientation.Left: BlockOrientation.Right,
        }

        blockOne = BlockNode(1)
        blockTwo = BlockNode(2)
        blockThree = BlockNode(3)
        blockFour = BlockNode(4)
        blockFive = BlockNode(5)
        blockSix = BlockNode(6)

        blockOne.neighbors[BlockOrientation.Up] = blockFive
        blockOne.neighbors[BlockOrientation.Right] = blockFour
        blockOne.neighbors[BlockOrientation.Down] = blockThree
        blockOne.neighbors[BlockOrientation.Left] = blockTwo

        blockTwo.neighbors[BlockOrientation.Up] = blockOne
        blockTwo.neighbors[BlockOrientation.Right] = blockThree
        blockTwo.neighbors[BlockOrientation.Down] = blockSix
        blockTwo.neighbors[BlockOrientation.Left] = blockFive

        blockThree.neighbors[BlockOrientation.Up] = blockOne
        blockThree.neighbors[BlockOrientation.Right] = blockFour
        blockThree.neighbors[BlockOrientation.Down] = blockSix
        blockThree.neighbors[BlockOrientation.Left] = blockTwo

        blockFour.neighbors[BlockOrientation.Up] = blockOne
        blockFour.neighbors[BlockOrientation.Right] = blockFive
        blockFour.neighbors[BlockOrientation.Down] = blockSix
        blockFour.neighbors[BlockOrientation.Left] = blockThree

        blockFive.neighbors[BlockOrientation.Up] = blockOne
        blockFive.neighbors[BlockOrientation.Right] = blockTwo
        blockFive.neighbors[BlockOrientation.Down] = blockSix
        blockFive.neighbors[BlockOrientation.Left] = blockFour

        blockSix.neighbors[BlockOrientation.Up] = blockThree
        blockSix.neighbors[BlockOrientation.Right] = blockFour
        blockSix.neighbors[BlockOrientation.Down] = blockFive
        blockSix.neighbors[BlockOrientation.Left] = blockTwo

        self.blocks = {
            1: blockOne,
            2: blockTwo,
            3: blockThree,
            4: blockFour,
            5: blockFive,
            6: blockSix,
        }
        
    def getPattern(self):
        number, orientation = self.face
        return self.patterns[number][orientation]

    ''' Bring your current face towards the UP orientation. '''
    def flipUp(self):
        number, orientation = self.face
        block = self.blocks[number].neighbors[self.opposites[orientation]]
        nextNumber = block.val
        self.face = (nextNumber, orientation)
        return self.face

    ''' 
        Bring your current face towards the DOWN orientation.
        (Opposite of whatever orientation we are in.)
    '''
    def flipDown(self):
        number, orientation = self.face
        if number == 5 and orientation == BlockOrientation.Up:
            block = self.blocks[number].neighbors[self.opposites[orientation]]
        else:
            block = self.blocks[number].neighbors[orientation]
        nextNumber = block.val
        self.face = (nextNumber, orientation)
        return self.face

    ''' Go left of your orientation. '''
    def flipRight(self):
        number, orientation = self.face
        leftOrientation = self.orientations[orientation].prev.val
        block = self.blocks[number].neighbors[leftOrientation]
        nextNumber = block.val
        self.face = (nextNumber, orientation)
        return self.face

    ''' Go right of your orientation. '''
    def flipLeft(self):
        number, orientation = self.face
        rightOrientation = self.orientations[orientation].next.val
        block = self.blocks[number].neighbors[rightOrientation]
        nextNumber = block.val
        self.face = (nextNumber, orientation)
        return self.face

    ''' Change orientation, but stay on the same face. '''
    def rotateRight(self):
        number, orientation = self.face
        nextOrientation = self.orientations[orientation].prev.val
        self.face = (number, nextOrientation)
        return self.face
        
    ''' Change orientation, but stay on the same face. '''
    def rotateLeft(self):
        number, orientation = self.face
        nextOrientation = self.orientations[orientation].next.val
        self.face = (number, nextOrientation)
        return self.face
