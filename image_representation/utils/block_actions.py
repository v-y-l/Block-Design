''' Go to the new face, if possible. '''
def goToFace(block, next_face):
    if next_face in block.getNeighbors():
        old_face = block.getFace()
        block.current_face = next_face
        printAction('[Go to face {}] '.format(next_face), block)
    else:
        raise Exception("Can't go from {} to {}".format(
            block.current_face, next_face))

''' Change orientation, but stay on the same face. '''
def rotateRight(block):
    old_pattern = block.getPattern()
    block.patterns[1] = block.orientations[block.patterns[1]].next.val
    block.patterns[6] = block.orientations[block.patterns[6]].next.val
    printAction('[Right rotate block] ', block)
        
''' Change orientation, but stay on the same face. '''
def rotateLeft(block):
    old_pattern = block.getPattern()
    block.patterns[1] = block.orientations[block.patterns[1]].prev.val
    block.patterns[6] = block.orientations[block.patterns[6]].prev.val
    printAction('[Left rotate block] ', block)

def printAction(actionPrefix, block):
    print(actionPrefix + str(block))
