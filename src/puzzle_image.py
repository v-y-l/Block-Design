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
        # Captures bottom right corner of a the block window,
        # with top left corner of picture as (0,0) and the
        # r and c growing larger rightwards and downwards.
        self.window_r = block_length
        self.window_c = block_length

    def getImage(self):
        return self.image

    def getWindow(self):
        return self.image[self.window_r-self.block_length:self.window_r][self.window_c-self.block_length:self.window_c]

    def getPattern(self):
        window = self.getWindow()
        a = window[int(self.block_length/4)][int(self.block_length/2)]
        b = window[int(self.block_length/2)][int(3*self.block_length/4)]
        c = window[int(3*self.block_length/4)][int(self.block_length/2)]
        d = window[int(self.block_length/2)][int(self.block_length/4)]
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
        for r in range(0, self.width, self.block_length):
            for c in range(0, self.width, self.block_length):
                self.window_r = r + self.block_length
                self.window_c = c + self.block_length
                puzzle.append(self.getPattern())
        self.window_r = self.block_length
        self.window_c = self.block_length
        return puzzle
        
