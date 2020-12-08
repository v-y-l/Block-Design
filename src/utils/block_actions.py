from numpy import rot90
from utils.constants import NUMBER_TO_GO_TO_FACE_ACTION, FACE_TO_COORDINATE
from utils.enums import BlockAction

''' Go to the new face, if possible. '''
def go_to_face(block, next_face):
    if next_face in block.get_neighbors():
        old_face = block.get_face()
        block.face = next_face
        block.r, block.c = FACE_TO_COORDINATE[block.orientation][block.face]
        if block.puzzle:
            block.puzzle.add_to_history(block.to_csv_row(NUMBER_TO_GO_TO_FACE_ACTION[next_face]))
    else:
        raise Exception("Can't go from {} to {}".format(
            block.face, next_face))

''' Change orientation, but stay on the same face. '''
def rotate_right(block):
    block.image = rot90(block.image, 3)
    block.orientation = block.block_orientations[block.orientation].next.val
    block.r, block.c = FACE_TO_COORDINATE[block.orientation][block.face]
    if block.puzzle: block.puzzle.add_to_history(block.to_csv_row(BlockAction.RotateRight))
        
''' Change orientation, but stay on the same face. '''
def rotate_left(block):
    block.image = rot90(block.image)
    block.orientation = block.block_orientations[block.orientation].prev.val
    block.r, block.c = FACE_TO_COORDINATE[block.orientation][block.face]
    if block.puzzle: block.puzzle.add_to_history(block.to_csv_row(BlockAction.RotateLeft))
