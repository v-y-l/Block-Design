from utils.enums import BlockOrientation, BlockAction

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

NUMBER_TO_GO_TO_FACE_ACTION = {
    1: BlockAction.GoToFaceOne,
    2: BlockAction.GoToFaceTwo,
    3: BlockAction.GoToFaceThree,
    4: BlockAction.GoToFaceFour,
    5: BlockAction.GoToFaceFive,
    6: BlockAction.GoToFaceSix,
}


PUZZLE_OPTIONS = {
    'puzzle_a': './puzzle_images/puzzle_a.png',
    'puzzle_b': './puzzle_images/puzzle_b.png',
    'puzzle_c': './puzzle_images/puzzle_c.png',
}

SHADE_BGR = [27, 13, 252]
WHITE_BGR = [255, 255, 255]
