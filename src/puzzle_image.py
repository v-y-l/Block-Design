from cv2 import imread, IMREAD_COLOR
from utils.enums import BlockPattern

class PuzzleImage:

    def __init__(self,
                 image_path='./puzzle_images/puzzle_a.png',
                 block_length=170,
                 shade_rgb=[27, 13, 252]):
        self.image = imread(image_path)
        self.height, self.width, _ = self.image.shape
        self.block_length = block_length
        self.shade_rgb = shade_rgb
        self.white_rgb = [255, 255, 255]
        # Captures top left corner of a the block window,
        # with top left corner of picture as (0,0) and the
        # r and c growing larger rightwards and downwards.
        self.window_r = 0
        self.window_c = 0

    def getImage(self):
        return self.image

    def getWindow(self):
        return self.image[self.window_r:self.window_r+self.block_length][self.window_c:self.window_c+self.block_length]

    def getPattern(self):
        a = self.image[self.window_r+int(self.block_length/4)][self.window_c+int(self.block_length/2)]
        b = self.image[self.window_r+int(self.block_length/2)][self.window_c+int(3*self.block_length/4)]
        c = self.image[self.window_r+int(3*self.block_length/4)][self.window_c+int(self.block_length/2)]
        d = self.image[self.window_r+int(self.block_length/2)][self.window_c+int(self.block_length/4)]
        if ((a == self.shade_rgb).all()) and ((b == self.shade_rgb).all()) and ((c == self.white_rgb).all()) and ((d == self.white_rgb).all()):
            return BlockPattern.BlackTopRightCornerSquare
        elif ((a == self.white_rgb).all()) and ((b == self.shade_rgb).all()) and ((c == self.shade_rgb).all()) and ((d == self.white_rgb).all()):
            return BlockPattern.BlackBottomRightCornerSquare
        elif ((a == self.white_rgb).all()) and ((b == self.white_rgb).all()) and ((c == self.shade_rgb).all()) and ((d == self.shade_rgb).all()):
            return BlockPattern.BlackBottomLeftCornerSquare
        elif ((a == self.shade_rgb).all()) and ((b == self.white_rgb).all()) and ((c == self.white_rgb).all()) and ((d == self.shade_rgb).all()):
            return BlockPattern.BlackTopLeftCornerSquare
        elif ((a == self.white_rgb).all()) and ((b == self.white_rgb).all()) and ((c == self.white_rgb).all()) and ((d == self.white_rgb).all()):
            return BlockPattern.WhiteSquare
        elif ((a == self.shade_rgb).all()) and ((b == self.shade_rgb).all()) and ((c == self.shade_rgb).all()) and ((d == self.shade_rgb).all()):
            return BlockPattern.BlackSquare
        else:
            raise Exception("Could not determine block pattern based on this sample: {}, {}, {}, {}".format(a, b, c, d))

    def getPuzzle(self):
        puzzle = []
        for r in range(0, self.height, self.block_length):
            self.window_r = r
            for c in range(0, self.width, self.block_length):
                self.window_c = c
                puzzle.append(self.getPattern())
        self.window_r = 0
        self.window_c = 0
        return puzzle
