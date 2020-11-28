from utils.enums import BlockPattern, BlockAction
from utils.data_structures import Node, FaceNode
from utils.block_actions import goToFace, rotateRight, rotateLeft
from utils.helper import isTrianglePattern

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
        self.printBlockInitialState()

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

        self.actionToFace = {
            BlockAction.GoToFaceOne: 1,
            BlockAction.GoToFaceTwo: 2,
            BlockAction.GoToFaceThree: 3,
            BlockAction.GoToFaceFour: 4,
            BlockAction.GoToFaceFive: 5,
            BlockAction.GoToFaceSix: 6
        }

        self.patterns = {
            1: BlockPattern.BlackTopRightCornerSquare,
            2: BlockPattern.WhiteSquare,
            3: BlockPattern.WhiteSquare,
            4: BlockPattern.BlackSquare,
            5: BlockPattern.BlackSquare,
            6: BlockPattern.BlackBottomRightCornerSquare,
        }

        self.actionCounter = {
            BlockAction.GoToFaceOne: 0,
            BlockAction.GoToFaceTwo: 0,
            BlockAction.GoToFaceThree: 0,
            BlockAction.GoToFaceFour: 0,
            BlockAction.GoToFaceFive: 0,
            BlockAction.GoToFaceSix: 0,
            BlockAction.RotateLeft: 0,
            BlockAction.RotateRight: 0
        }
        
    ''' Sets up data structures for enabling rotation logic. '''
    def _setupRotationDataStructures(self):
        blackTopRightCornerSquare = Node(BlockPattern.BlackTopRightCornerSquare)
        blackBottomRightCornerSquare = Node(BlockPattern.BlackBottomRightCornerSquare)
        blackBottomLeftCornerSquare = Node(BlockPattern.BlackBottomLeftCornerSquare)
        blackTopLeftCornerSquare = Node(BlockPattern.BlackTopLeftCornerSquare)
        whiteSquare = Node(BlockPattern.WhiteSquare)
        blackSquare = Node(BlockPattern.BlackSquare)

        whiteSquare.next = whiteSquare
        whiteSquare.prev = whiteSquare
        blackSquare.next = blackSquare
        blackSquare.prev = blackSquare
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
            BlockPattern.BlackTopLeftCornerSquare: blackTopLeftCornerSquare,
            BlockPattern.BlackSquare: blackSquare,
            BlockPattern.WhiteSquare: whiteSquare,
        }

    ''' Setup data structures that enable movement to a neighboring face. '''
    def _setupGoToDataStructures(self):
        faceOne = FaceNode(1)
        faceTwo = FaceNode(2)
        faceThree = FaceNode(3)
        faceFour = FaceNode(4)
        faceFive = FaceNode(5)
        faceSix = FaceNode(6)

        faceOne.neighbors = {5, 4, 3, 2}
        faceTwo.neighbors = {1, 3, 6, 5}
        faceThree.neighbors = {1, 4, 6, 2}
        faceFour.neighbors = {1, 5, 6, 3}
        faceFive.neighbors = {1, 2, 6, 4}
        faceSix.neighbors = {3, 4, 5, 2}

        self.faces = {
            1: faceOne,
            2: faceTwo,
            3: faceThree,
            4: faceFour,
            5: faceFive,
            6: faceSix,
        }

    def getNeighbors(self):
        return self.faces[self.current_face].neighbors

    def getFace(self):
        return self.current_face

    def getNumber(self):
        return self.block_number
        
    def getPattern(self):
        return self.patterns[self.current_face]

    def peekAction(self, action):
        if action not in self.getValidActions():
            raise Exception("Invalid action {} for {}".format(action, str(self)))
        if action == BlockAction.RotateLeft:
            return self.orientations[self.getPattern()].prev.val
        elif action == BlockAction.RotateRight:
            return self.orientations[self.getPattern()].next.val
        else:
            return self.patterns[self.actionToFace[action]]

    def executeAction(self, action):
        self.actionCounter[action] += 1
        self.actions[action]()
        
    def getValidActions(self):
        return self.getRotateActions() + self.getGoToActions()

    def getRotateActions(self):
        return [BlockAction.RotateLeft, BlockAction.RotateRight]

    def getGoToActions(self):
        return [self.goToFaceAction[face] for face in self.getNeighbors()]

    def hasTrianglePattern(self):
        return isTrianglePattern(self.getPattern())

    def printBlockInitialState(self):
        print('[Instantiate block] ' + str(self))

    def getActionCounter(self):
        return self.actionCounter

    def __str__(self):
        return 'Block {} state: face {}, pattern {}'.format(
            self.getNumber(), self.getFace(), self.getPattern())