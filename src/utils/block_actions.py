from numpy import rot90
from utils.constants import NUMBER_TO_WORD, FACE_TO_COORDINATE
from utils.helper import to_csv_row

''' Go to the new face, if possible. '''
def go_to_face(block, next_face):
    if next_face in block.get_neighbors():
        old_face = block.get_face()
        block.face = next_face
        block.r, block.c = FACE_TO_COORDINATE[block.orientation][block.face]
        return to_csv_row('GoToFace{},'.format(NUMBER_TO_WORD[next_face]), block)
    else:
        raise Exception("Can't go from {} to {}".format(
            block.face, next_face))

''' Change orientation, but stay on the same face. '''
def rotate_right(block):
    block.image = rot90(block.image, 3)
    block.orientation = block.block_orientations[block.orientation].next.val
    block.r, block.c = FACE_TO_COORDINATE[block.orientation][block.face]
    return to_csv_row('RightRotate,', block)
        
''' Change orientation, but stay on the same face. '''
def rotate_left(block):
    block.image = rot90(block.image)
    block.orientation = block.block_orientations[block.orientation].prev.val
    block.r, block.c = FACE_TO_COORDINATE[block.orientation][block.face]
    return to_csv_row('LeftRotate,', block)
