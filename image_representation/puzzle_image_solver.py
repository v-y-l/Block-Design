from cv2 import imread, cvtColor, COLOR_BGR2RGB
from PIL import Image
from utils.enums import BlockPattern, SearchType, BlockAction
from utils.helper import getPattern, block_length
from search import random_search, sequential_search
from block_image import BlockImage

class PuzzleImageSolver:

    def __init__(self,
                 image_path='./puzzle_images/puzzle_a.png',
                 solvers={
                     SearchType.Face: random_search,
                     SearchType.PuzzlePiece: sequential_search
                 }
    ):
        self.image = imread(image_path)
        self.height, self.width, _ = self.image.shape
        # Captures top left corner of a the block window,
        # with top left corner of picture as (0,0) and the
        # r and c growing larger rightwards and downwards.
        self.r = 0
        self.c = 0
    
        self.solvers = solvers
        self.problem = self.getPuzzle()
        self.blockBank = [BlockImage(1, i+1) for i in range(len(self.problem))]
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

    def getWindow(self):
        rowOffset = getRowOffset(self.r, self.c, 1)
        colOffset = getColOffset(self.r, self.c, 1)
        return self.image[self.r:rowOffset][self.c:colOffset]

    def getPattern(self):
        return getPattern(self.r, self.c, self.image)

    def getPuzzle(self):
        puzzle = []
        for r in range(0, self.height, block_length):
            self.r = r
            for c in range(0, self.width, block_length):
                self.c = c
                puzzle.append(self.getPattern())
        self.r = 0
        self.c = 0
        return puzzle

    def getImage(self):
        return self.image

    def showImage(self):
        Image.fromarray(cvtColor(self.image, COLOR_BGR2RGB), 'RGB').show()

    '''
    Returns a list of actions executed by each block to solve the problem.
    '''
    def solve(self):
        faceSearcher = self.solvers[SearchType.Face]
        puzzlePieceSearcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actionsPerBlock = []

        for i in puzzlePieceSearcher(self.problem):
            block = self.blockBank[i]
            searchFaceActions = faceSearcher(
                block,
                self.problem[i],
                actionsPerBlock)
            self.addBlockToStats(block)
            self.printSolvedPuzzlePiece(i)
        self.printPuzzleStats()

        return actionsPerBlock

    def addBlockToStats(self, block):
        for action, count in block.getActionCounter().items():
            self.actionCounter[action] += count

    def printSolvedPuzzlePiece(self, pieceNumber):
        print("...[Solved puzzle piece {}] {}\n".format(
            pieceNumber + 1,
            str(self.blockBank[pieceNumber])))

    def getActionCounter(self):
        return self.actionCounter

    def printPuzzleStats(self):
        print('========================')
        print('| Puzzle statistics... |')
        print('========================')
        for action, count in self.getActionCounter().items():
            print(action, ": ", count)

puzzle_options = {
    'a': PuzzleImageSolver(
        './puzzle_images/puzzle_a.png',
    ),
    'b': PuzzleImageSolver(
        './puzzle_images/puzzle_b.png',
    ),
    'c': PuzzleImageSolver(
        './puzzle_images/puzzle_c.png',
    )
}
