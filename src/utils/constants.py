from utils.enums import BlockOrientation

BLOCK_LENGTH = 170

# Give a 5 pixel leeway to the potentially overcropped image
EDGE_OFFSET = 5

# Coordinates are represented row by column.
FACE_TO_COORDINATE = {
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

NUMBER_TO_WORD = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six'
}

SHADE_BGR = [27, 13, 252]
WHITE_BGR = [255, 255, 255]
