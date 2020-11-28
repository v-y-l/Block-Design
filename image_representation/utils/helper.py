from utils.enums import BlockPattern, BlockOrientation

shade_bgr = [27, 13, 252]
white_bgr = [255, 255, 255]
block_length = 170

def getColOffset(r, c, multiplier):
    return c + int(block_length * multiplier)

def getRowOffset(r, c, multiplier):
    return r + int(block_length * multiplier)

def getPattern(row, col, block_image):
    a = block_image[getRowOffset(row, col, .25)][getColOffset(row, col, .5)]
    b = block_image[getRowOffset(row, col, .5)][getColOffset(row, col, .75)]
    c = block_image[getRowOffset(row, col, .75)][getColOffset(row, col, .5)]
    d = block_image[getRowOffset(row, col, .5)][getColOffset(row, col, .25)]
    if (
            ((a == shade_bgr).all())
            and ((b == shade_bgr).all())
            and ((c == white_bgr).all())
            and ((d == white_bgr).all())
    ):
        return BlockPattern.BlackTopRightCornerSquare
    elif (
                ((a == white_bgr).all())
            and ((b == shade_bgr).all())
            and ((c == shade_bgr).all())
            and ((d == white_bgr).all())
    ):
        return BlockPattern.BlackBottomRightCornerSquare
    elif (
                ((a == white_bgr).all())
            and ((b == white_bgr).all())
            and ((c == shade_bgr).all())
            and ((d == shade_bgr).all())
    ):
            return BlockPattern.BlackBottomLeftCornerSquare
    elif (
                ((a == shade_bgr).all())
            and ((b == white_bgr).all())
            and ((c == white_bgr).all())
            and ((d == shade_bgr).all())
    ):
        return BlockPattern.BlackTopLeftCornerSquare
    elif (
                ((a == white_bgr).all())
            and ((b == white_bgr).all())
            and ((c == white_bgr).all())
            and ((d == white_bgr).all())
    ):
        return BlockPattern.WhiteSquare
    elif (
                ((a == shade_bgr).all())
            and ((b == shade_bgr).all())
            and ((c == shade_bgr).all())
            and ((d == shade_bgr).all())
    ):
        return BlockPattern.BlackSquare
    else:
        raise Exception("Could not determine block pattern " +
                        "based on this sample: \na={}, \nb={}, \nc={}, \nd={}".format(a, b, c, d))

''' Check if the block has a triangle pattern. '''    
def isTrianglePattern(pattern):
    return pattern == BlockPattern.BlackTopLeftCornerSquare or pattern == BlockPattern.BlackTopRightCornerSquare or pattern == BlockPattern.BlackBottomLeftCornerSquare or pattern == BlockPattern.BlackBottomRightCornerSquare

'''
Coordinates are represented row by column.
'''
face_to_coordinate = {
    BlockOrientation.Up: {
        1: (0, 170),
        2: (170, 0),
        3: (170, 170),
        4: (170, 340),
        5: (170, 510),
        6: (340, 170)
    },
    BlockOrientation.Right: {
        1: (170, 340),
        2: (0, 170),
        3: (170, 170),
        4: (340, 170),
        5: (510, 170),
        6: (170, 0),
    },
    BlockOrientation.Down: {
        1: (340, 340),
        2: (170, 510),
        3: (170, 340),
        4: (170, 170),
        5: (170, 0),
        6: (0, 340),
    },
    BlockOrientation.Left: {
        1: (340, 0),
        2: (510, 170),
        3: (340, 170),
        4: (170, 170),
        5: (0, 170),
        6: (340, 340),
    },
}
