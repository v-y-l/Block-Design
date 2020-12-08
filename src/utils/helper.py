from utils.enums import BlockPattern, BlockOrientation
from utils.constants import BLOCK_LENGTH, SHADE_BGR, WHITE_BGR

def get_col_offset(r, c, multiplier):
    return c + int(BLOCK_LENGTH * multiplier)

def get_row_offset(r, c, multiplier):
    return r + int(BLOCK_LENGTH * multiplier)

def get_pattern(row, col, block_image):
    a = block_image[get_row_offset(row, col, .25)][get_col_offset(row, col, .5)]
    b = block_image[get_row_offset(row, col, .5)][get_col_offset(row, col, .75)]
    c = block_image[get_row_offset(row, col, .75)][get_col_offset(row, col, .5)]
    d = block_image[get_row_offset(row, col, .5)][get_col_offset(row, col, .25)]
    if (
            ((a == SHADE_BGR).all())
            and ((b == SHADE_BGR).all())
            and ((c == WHITE_BGR).all())
            and ((d == WHITE_BGR).all())
    ):
        return BlockPattern.BlackTopRightCornerSquare
    elif (
                ((a == WHITE_BGR).all())
            and ((b == SHADE_BGR).all())
            and ((c == SHADE_BGR).all())
            and ((d == WHITE_BGR).all())
    ):
        return BlockPattern.BlackBottomRightCornerSquare
    elif (
                ((a == WHITE_BGR).all())
            and ((b == WHITE_BGR).all())
            and ((c == SHADE_BGR).all())
            and ((d == SHADE_BGR).all())
    ):
            return BlockPattern.BlackBottomLeftCornerSquare
    elif (
                ((a == SHADE_BGR).all())
            and ((b == WHITE_BGR).all())
            and ((c == WHITE_BGR).all())
            and ((d == SHADE_BGR).all())
    ):
        return BlockPattern.BlackTopLeftCornerSquare
    elif (
                ((a == WHITE_BGR).all())
            and ((b == WHITE_BGR).all())
            and ((c == WHITE_BGR).all())
            and ((d == WHITE_BGR).all())
    ):
        return BlockPattern.WhiteSquare
    elif (
                ((a == SHADE_BGR).all())
            and ((b == SHADE_BGR).all())
            and ((c == SHADE_BGR).all())
            and ((d == SHADE_BGR).all())
    ):
        return BlockPattern.BlackSquare
    else:
        return BlockPattern.Unknown
    
''' Check if the block has a triangle pattern. '''    
def is_triangle_pattern(pattern):
    return (
        pattern == BlockPattern.BlackTopLeftCornerSquare or
        pattern == BlockPattern.BlackTopRightCornerSquare or
        pattern == BlockPattern.BlackBottomLeftCornerSquare or
        pattern == BlockPattern.BlackBottomRightCornerSquare
    )

def to_csv_row(action_prefix, block):
    return str(block) + "action," + action_prefix
