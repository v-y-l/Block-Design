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

    def __init__(self, number=1):
        
        self.current_face = number
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
            blackTopRightCornerSquare: blackTopRightCornerSquare,
            blackBottomRightCornerSquare: blackBottomRightCornerSquare,
            blackBottomLeftCornerSquare: blackBottomLeftCornerSquare,
            blackTopLeftCornerSquare: blackTopLeftCornerSquare
        }

        # For movement to neighboring faces

        blockOne = BlockNode(1)
        blockTwo = BlockNode(2)
        blockThree = BlockNode(3)
        blockFour = BlockNode(4)
        blockFive = BlockNode(5)
        blockSix = BlockNode(6)

        blockOne.neighbors = {blockFive, blockFour, blockThree, blockTwo}
        blockTwo.neighbors = {blockOne, blockThree, blockSix, blockFive}
        blockThree.neighbors = {blockOne, blockFour, blockSix, blockTwo}
        blockFour.neighbors = {blockOne, blockFive, blockSix, blockThree}
        blockFive.neighbors = {blockOne, blockTwo, blockSix, blockFour}
        blockSix.neighbors = {blockThree, blockFour, blockFive, blockTwo}

        self.blocks = {
            1: blockOne,
            2: blockTwo,
            3: blockThree,
            4: blockFour,
            5: blockFive,
            6: blockSix,
        }

    def getNeighbors(self):
        return self.blocks[self.current_face].neighbors
        
    def getPattern(self):
        return self.patterns[self.current_face]

    ''' Go to the new face, if possible. '''
    def goToFace(self, next_face):
        if next_face in self.getNeighbors():
            self.current_face = next_face
        else:
            raise Exception("Can't go from {} to {}".format(self.current_face, next_face))

    ''' Change orientation, but stay on the same face. '''
    def rotateRight(self):
        self.patterns[1] = self.orientations[self.patterns[1]].next
        self.patterns[6] = self.orientations[self.patterns[6]].next
                
    ''' Change orientation, but stay on the same face. '''
    def rotateLeft(self):
        self.patterns[1] = self.orientations[self.patterns[1]].prev
        self.patterns[6] = self.orientations[self.patterns[6]].prev

