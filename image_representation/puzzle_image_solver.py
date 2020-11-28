from cv2 import imread
from utils.enums import BlockPattern
from utils.helper import getPattern, block_length

class PuzzleImageSolver:

    def __init__(self, image_path='./puzzle_images/puzzle_a.png'):
        self.image = imread(image_path)
        self.height, self.width, _ = self.image.shape
        # Captures top left corner of a the block window,
        # with top left corner of picture as (0,0) and the
        # r and c growing larger rightwards and downwards.
        self.r = 0
        self.c = 0

    def getImage(self):
        return self.image

    def getWindow(self):
        return self.image[self.r:getRowOffset(self.r, self.c, 1)][self.c:getColOffset(self.r, self.c, 1)]

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
