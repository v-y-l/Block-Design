from utils.enums import BlockPattern

shade_rgb = [27, 13, 252]
white_rgb = [255, 255, 255]
block_length = 170

def getColOffset(r, c, multiplier):
    return c + int(block_length * multiplier)

def getRowOffset(r, c, multiplier):
    return r + int(block_length * multiplier)

def getPattern(r, c, block_image):
    a = block_image[getRowOffset(r, c, .25)][getColOffset(r, c, .5)]
    b = block_image[getRowOffset(r, c, .5)][getColOffset(r, c, .75)]
    c = block_image[getRowOffset(r, c, .75)][getColOffset(r, c, .5)]
    d = block_image[getRowOffset(r, c, .5)][getColOffset(r, c, .25)]
    if (
            ((a == shade_rgb).all())
            and ((b == shade_rgb).all())
            and ((c == white_rgb).all())
            and ((d == white_rgb).all())
    ):
        return BlockPattern.BlackTopRightCornerSquare
    elif (
                ((a == white_rgb).all())
            and ((b == shade_rgb).all())
            and ((c == shade_rgb).all())
            and ((d == white_rgb).all())
    ):
        return BlockPattern.BlackBottomRightCornerSquare
    elif (
                ((a == white_rgb).all())
            and ((b == white_rgb).all())
            and ((c == shade_rgb).all())
            and ((d == shade_rgb).all())
    ):
            return BlockPattern.BlackBottomLeftCornerSquare
    elif (
                ((a == shade_rgb).all())
            and ((b == white_rgb).all())
            and ((c == white_rgb).all())
            and ((d == shade_rgb).all())
    ):
        return BlockPattern.BlackTopLeftCornerSquare
    elif (
                ((a == white_rgb).all())
            and ((b == white_rgb).all())
            and ((c == white_rgb).all())
            and ((d == white_rgb).all())
    ):
        return BlockPattern.WhiteSquare
    elif (
                ((a == shade_rgb).all())
            and ((b == shade_rgb).all())
            and ((c == shade_rgb).all())
            and ((d == shade_rgb).all())
    ):
        return BlockPattern.BlackSquare
    else:
        raise Exception("Could not determine block pattern " +
                        "based on this sample: {}, {}, {}, {}".format(a, b, c, d))

''' Check if the block has a triangle pattern. '''    
def isTrianglePattern(pattern):
    return pattern == BlockPattern.BlackTopLeftCornerSquare or pattern == BlockPattern.BlackTopRightCornerSquare or pattern == BlockPattern.BlackBottomLeftCornerSquare or pattern == BlockPattern.BlackBottomRightCornerSquare
