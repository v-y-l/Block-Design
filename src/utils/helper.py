from utils.enums import BlockPattern

''' Check if the block has a triangle pattern. '''    
def isTrianglePattern(pattern):
    return pattern == BlockPattern.BlockBlackTopLeftCornerSquare or pattern == BlockPattern.BlackTopRightCornerSquare or pattern == BlockPattern.BlackBottomLeftCornerSquarep or pattern == BlockPattern.BlackBottomRightCornerSquare
