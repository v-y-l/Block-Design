from utils.enums import BlockPattern, BlockOrientation

SHADE_BGR = [27, 13, 252]
WHITE_BGR = [255, 255, 255]
EDGE_OFFSET = 5 # Give a 5 pixel leeway to the potentially overcropped image
BLOCK_LENGTH = 170

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
