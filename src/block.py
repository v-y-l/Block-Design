from utils.enums import BlockPattern, BlockAction
from utils.data_structures import Node, BlockNode
from utils.block_actions import goToFace, rotateRight, rotateLeft

'''
A block has six faces. Each face is assigned a number.
We represent things two dimensionally by sprawling out the faces.
This simplifies tracking rotation state, as we can apply rotations
across the entire 2D image.

                        [   BlackTopRightCornerSquare (1)  ]
    [ WhiteSquare (2) ] [          WhiteSquare (3)         ] [ BlackSquare (4) ] [ BlackSquare (5) ]
                        [ BlackBottomRightCornerSquare (6) ]

'''
class Block:

    def __init__(self, face=1, number=1):
        self.current_face = face
        self.block_number = number
        self._setupBlockDataStructures()
        self._setupRotationDataStructures()
        self._setupGoToDataStructures()
        print(str(self))

    '''
    Setup the data structures that coordinate between the different
    block concepts.
    '''
    def _setupBlockDataStructures(self):
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

        self.patterns = {
            1: BlockPattern.BlackTopRightCornerSquare,
            2: BlockPattern.WhiteSquare,
            3: BlockPattern.WhiteSquare,
            4: BlockPattern.BlackSquare,
            5: BlockPattern.BlackSquare,
            6: BlockPattern.BlackBottomRightCornerSquare,
        }

        
    ''' Sets up data structures for enabling rotation logic. '''
    def _setupRotationDataStructures(self):
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

    ''' Setup data structures that enable movement to a neighboring face. '''
    def _setupGoToDataStructures(self):
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

    def __str__(self):
        return 'Block {}: face {}, pattern {}'.format(
            self.getNumber(), self.getFace(), self.getPattern())
