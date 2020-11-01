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

                        [   BlackTopRightCornerSquare (1)  ]
    [ WhiteSquare (2) ] [          WhiteSquare (3)         ] [ BlackSquare (4) ] [ BlackSquare (5) ]
                        [ BlackBottomRightCornerSquare (6) ]

'''
class Block:

    def __init__(self, face=1, number=1):
        self.current_face = face
        self.block_number = number
        self.patterns = {
            1: BlockPattern.BlackTopRightCornerSquare,
            2: BlockPattern.WhiteSquare,
            3: BlockPattern.WhiteSquare,
            4: BlockPattern.BlackSquare,
            5: BlockPattern.BlackSquare,
            6: BlockPattern.BlackBottomRightCornerSquare,
        }

        # For rotations

        blackTopRightCornerSquare = Node(BlockPattern.BlackTopRightCornerSquare)
        blackBottomRightCornerSquare = Node(BlockPattern.BlackBottomRightCornerSquare)
        blackBottomLeftCornerSquare = Node(BlockPattern.BlackBottomLeftCornerSquare)
        blackTopLeftCornerSquare = Node(BlockPattern.BlackTopLeftCornerSquare)

        blackTopRightCornerSquare.next = blackBottomRightCornerSquare
        blackTopRightCornerSquare.prev = blackTopLeftCornerSquare
        blackBottomRightCornerSquare.next = blackBottomLeftCornerSquare
        blackBottomRightCornerSquare.prev = blackTopRightCornerSquare
        blackBottomLeftCornerSquare.next = blackTopLeftCornerSquare
        blackBottomLeftCornerSquare.prev = blackBottomRightCornerSquare
        blackTopLeftCornerSquare.next = blackTopRightCornerSquare
        blackTopLeftCornerSquare.prev = blackBottomLeftCornerSquare

        self.orientations = {
            BlockPattern.BlackTopRightCornerSquare: blackTopRightCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare: blackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare: blackBottomLeftCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare: blackTopLeftCornerSquare
        }

        # For movement to neighboring faces

        blockOne = BlockNode(1)
        blockTwo = BlockNode(2)
        blockThree = BlockNode(3)
        blockFour = BlockNode(4)
        blockFive = BlockNode(5)
        blockSix = BlockNode(6)

        blockOne.neighbors = {5, 4, 3, 2}
        blockTwo.neighbors = {1, 3, 6, 5}
        blockThree.neighbors = {1, 4, 6, 2}
        blockFour.neighbors = {1, 5, 6, 3}
        blockFive.neighbors = {1, 2, 6, 4}
        blockSix.neighbors = {3, 4, 5, 2}

        self.blocks = {
            1: blockOne,
            2: blockTwo,
            3: blockThree,
            4: blockFour,
            5: blockFive,
            6: blockSix,
        }

        self.actions = {
            BlockAction.GoToFaceOne: lambda: goToFace(self, 1),
            BlockAction.GoToFaceTwo: lambda: goToFace(self, 2),
            BlockAction.GoToFaceThree: lambda: goToFace(self, 3),
            BlockAction.GoToFaceFour: lambda: goToFace(self, 4),
            BlockAction.GoToFaceFive: lambda: goToFace(self, 5),
            BlockAction.GoToFaceSix: lambda: goToFace(self, 6),
            BlockAction.RotateLeft: lambda: rotateLeft(self),
            BlockAction.RotateRight: lambda: rotateRight(self)
        }

        self.goToFaceAction = {
            1: BlockAction.GoToFaceOne,
            2: BlockAction.GoToFaceTwo,
            3: BlockAction.GoToFaceThree,
            4: BlockAction.GoToFaceFour,
            5: BlockAction.GoToFaceFive,
            6: BlockAction.GoToFaceSix
        }

    def getNeighbors(self):
        return self.blocks[self.current_face].neighbors

    def getFace(self):
        return self.current_face

    def getNumber(self):
        return self.block_number
        
    def getPattern(self):
        return self.patterns[self.current_face]

    def executeAction(self, action):
        self.actions[action]()
        
    def getValidActions(self):
        rotateActions =  [BlockAction.RotateLeft, BlockAction.RotateRight]
        goToActions = [self.goToFaceAction[face] for face in self.getNeighbors()]
        return rotateActions + goToActions
    
''' Go to the new face, if possible. '''
def goToFace(block, next_face):
    if next_face in block.getNeighbors():
        block.current_face = next_face
        print('goTo: block {}, face {}, pattern {}'
          .format(block.getNumber(), block.getFace(), block.getPattern()))
    else:
        raise Exception("Can't go from {} to {}".format(
            block.current_face, next_face))

''' Change orientation, but stay on the same face. '''
def rotateRight(block):
    block.patterns[1] = block.orientations[block.patterns[1]].next.val
    block.patterns[6] = block.orientations[block.patterns[6]].next.val
    print('rotateRight: block {}, face {}, pattern {}'
          .format(block.getNumber(), block.getFace(), block.getPattern()))
        
''' Change orientation, but stay on the same face. '''
def rotateLeft(block):
    block.patterns[1] = block.orientations[block.patterns[1]].prev.val
    block.patterns[6] = block.orientations[block.patterns[6]].prev.val
    print('rotateLeft: block {}, face {}, pattern {}'
          .format(block.getNumber(), block.getFace(), block.getPattern()))
