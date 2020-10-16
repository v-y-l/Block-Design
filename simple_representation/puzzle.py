from block import Pattern, Block
from random import sample

class Puzzle:

    def __init__(self, dest, searcher):
        self.searcher = searcher
        self.dest = dest
        self.blocks = len(dest)*[0]
        for i, _ in enumerate(dest):
            dest[i] = Block()

    def solve(self):
        moves = []
        for i in range(len(dest)):
            moves.extend(
                self.searcher(self.blocks[i], self.dest[i]))
        return moves

def random_search(block, dest_pattern):
    moves = []
    if block.getPattern() == dest_pattern:
        return moves

    next_face = sample(block.getNeighbors(), 1)[0]
    moves.append(next_face)
    block.goToFace(next_face)
    return random_search(block, dest_pattern)
