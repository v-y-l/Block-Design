from block import Pattern, Block

class Puzzle:

    def __init__(self, dest):
        self.dest = dest
        self.blocks = len(dest)*[0]
        for i, _ in enumerate(dest):
            dest[i] = Block()
