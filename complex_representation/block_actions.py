''' Go to the new face, if possible. '''
def goToFace(block, next_face):
    if next_face in block.getNeighbors():
        block.current_face = next_face
        print('Go to: ' + str(block))
    else:
        raise Exception("Can't go from {} to {}".format(
            block.current_face, next_face))

''' Change orientation, but stay on the same face. '''
def rotateRight(block):
    block.patterns[1] = block.orientations[block.patterns[1]].next.val
    block.patterns[6] = block.orientations[block.patterns[6]].next.val
    print('Right rotate: ' + str(block))
        
''' Change orientation, but stay on the same face. '''
def rotateLeft(block):
    block.patterns[1] = block.orientations[block.patterns[1]].prev.val
    block.patterns[6] = block.orientations[block.patterns[6]].prev.val
    print('Left rotate: ' + str(block))
