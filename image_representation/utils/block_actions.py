from numpy import rot90

''' Go to the new face, if possible. '''
def goToFace(block, next_face):
    if next_face in block.getNeighbors():
        old_face = block.getFace()
        block.face = next_face
        block.r, block.c = block.face_to_coordinate[block.orientation][block.face]
        printAction('[Go to face {}] '.format(next_face), block)
    else:
        raise Exception("Can't go from {} to {}".format(
            block.face, next_face))

''' Change orientation, but stay on the same face. '''
def rotateRight(block):
    block.block_image = rot90(block.image, 3)
    block.orientation = block.blockOrientations[block.orientation].next
    block.r, block.c = block.face_to_coordinate[block.orientation][block.face]
    printAction('[Right rotate block] ', block)
        
''' Change orientation, but stay on the same face. '''
def rotateLeft(block):
    block.block_image = rot90(block.image)
    block.orientation = block.blockOrientations[block.orientation].next
    block.r, block.c = block.face_to_coordinate[block.orientation][block.face]
    printAction('[Left rotate block] ', block)

def printAction(actionPrefix, block):
    print(actionPrefix + str(block))
