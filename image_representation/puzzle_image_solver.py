from cv2 import imread, cvtColor, COLOR_BGR2RGB
from PIL import Image
from utils.enums import BlockPattern, SearchType, BlockAction, PuzzleAction
from utils.helper import getPattern, block_length, edge_offset
from search import random_search, sequential_search
from block_image import BlockImage
import numpy as np

class PuzzleImageSolver:

    def __init__(self,
                 image_path='./puzzle_images/puzzle_a.png',
                 solvers={
                     SearchType.Face: random_search,
                     SearchType.PuzzlePiece: sequential_search
                 },
                 config={
                     # Value from 0 to 1, represents % of memory
                     # loss on the puzzle each turn
                     'puzzle_memory_loss_factor': .5
                 }
    ):
        self.image_path = image_path
        self.image = imread(image_path)
        self.height, self.width, _ = self.image.shape
        # Captures top left corner of a the block window,
        # with top left corner of picture as (0,0) and the
        # r and c growing larger rightwards and downwards.
        self.r = 0
        self.c = 0
    
        self.solvers = solvers
        self.config = config
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
            BlockAction.RotateRight: 0,
            BlockAction.PickUpBlock: 0,
            BlockAction.PlaceInPuzzle: 0,
            PuzzleAction.LookAtPuzzle: 0,
        }

    def getWindow(self):
        rowOffset = getRowOffset(self.r, self.c, 1)
        colOffset = getColOffset(self.r, self.c, 1)
        return self.image[self.r:rowOffset][self.c:colOffset]

    def getPattern(self):
        return getPattern(self.r, self.c, self.image)

    def getPuzzle(self):
        puzzle = []
        for r in range(0, self.height - edge_offset, block_length):
            self.r = r
            for c in range(0, self.width - edge_offset, block_length):
                self.c = c
                puzzle.append(self.getPattern())
        self.r = 0
        self.c = 0
        return puzzle

    ''' Returns a numpy array with shape of height x width x bgr pixels. '''
    def getImage(self):
        return self.image

    ''' Opens the puzzle as an image. '''
    def showImage(self):
        Image.fromarray(cvtColor(self.image, COLOR_BGR2RGB), 'RGB').show()

    ''' Sets a memory_loss_factor amount of the image to black to simulate forgetfulness. '''
    def forget(self, memory_loss_factor):
        if (memory_loss_factor) == 0: return
        height, width, bgr_len = self.image.shape
        total_pixels = height * width
        total_pixels_to_forget = int(total_pixels * memory_loss_factor)
        tmp_image = self.image.reshape(total_pixels, bgr_len)
        mask = np.ones((total_pixels, bgr_len), np.uint8)
        mask[:total_pixels_to_forget] = [0, 0, 0]
        np.random.shuffle(mask)
        tmp_image *= mask
        self.image = tmp_image.reshape(height, width, bgr_len)
        self.problem = self.getPuzzle()

    ''' Take a look at the puzzle to refresh our memory of it. '''
    def remember(self):
        self.image = imread(self.image_path)
        self.problem = self.getPuzzle()

    ''' Returns a list of actions executed by each block to solve the problem. '''
    def solve(self):
        faceSearcher = self.solvers[SearchType.Face]
        puzzlePieceSearcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actionsPerBlock = []
        puzzlePieceIndices = puzzlePieceSearcher(self.problem)
        for i in puzzlePieceIndices:
            block = self.blockBank[i]
            searchFaceActions = faceSearcher(
                block,
                self.problem[i],
                actionsPerBlock)
            if (len(searchFaceActions) == 0):
                self.actionCounter[PuzzleAction.LookAtPuzzle] += 1
                self.remember()
                searchFaceActions = faceSearcher(
                    block,
                    self.problem[i],
                    actionsPerBlock)
            self.forget(self.config["puzzle_memory_loss_factor"])
            self.addBlockToStats(block)
            self.printSolvedPuzzlePiece(i)
        self.printPuzzleStats()
        return actionsPerBlock

    ''' Calculates the total and individual number of executed moves. '''
    def addBlockToStats(self, block):
        for action, count in block.getActionCounter().items():
            self.actionCounter[action] += count
        self.actionCounter[BlockAction.PickUpBlock] += 1
        self.actionCounter[BlockAction.PlaceInPuzzle] += 1

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
        totalActionCount = 0
        for action, count in self.getActionCounter().items():
            print(action, ": ", count)
            totalActionCount += count
        print("Total actions taken: {}".format(totalActionCount))

puzzle_options = {
    'a': './puzzle_images/puzzle_a.png',
    'b': './puzzle_images/puzzle_b.png',
    'c': './puzzle_images/puzzle_c.png',
}
