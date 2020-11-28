from utils.enums import BlockPattern

''' Check if the block has a triangle pattern. '''    
def isTrianglePattern(pattern):
    return pattern == BlockPattern.BlackTopLeftCornerSquare or pattern == BlockPattern.BlackTopRightCornerSquare or pattern == BlockPattern.BlackBottomLeftCornerSquare or pattern == BlockPattern.BlackBottomRightCornerSquare
