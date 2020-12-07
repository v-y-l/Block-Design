from numpy import rot90

''' _go to the new face, if possible. '''
def go_to_face(block, next_face):
    if next_face in block.get_neighbors():
        old_face = block.get_face()
        block.face = next_face
        block.r, block.c = block.face_to_coordinate[block.orientation][block.face]
        print_action('[Go to face {}] '.format(next_face), block)
    else:
        raise Exception("Can't go from {} to {}".format(
            block.face, next_face))

''' _change orientation, but stay on the same face. '''
def rotate_right(block):
    block.image = rot90(block.image, 3)
    block.orientation = block.block_orientations[block.orientation].next.val
    block.r, block.c = block.face_to_coordinate[block.orientation][block.face]
    print_action('[Right rotate block] ', block)
        
''' _change orientation, but stay on the same face. '''
def rotate_left(block):
    block.image = rot90(block.image)
    block.orientation = block.block_orientations[block.orientation].prev.val
    block.r, block.c = block.face_to_coordinate[block.orientation][block.face]
    print_action('[Left rotate block] ', block)

def print_action(action_prefix, block):
    print(action_prefix + str(block))
