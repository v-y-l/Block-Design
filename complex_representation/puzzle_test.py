import unittest

from block import BlockPattern, Block
from puzzle import Puzzle, random_search

class TestBlockMethods(unittest.TestCase):

    def test_init(self):
        puzzle = Puzzle([
            BlockPattern.BlackSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackSquare
        ], random_search)
        self.assertEqual(len(puzzle.blockBank), 4)

    def test_random_search(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(),
                         BlockPattern.BlackTopRightCornerSquare)
        random_search(block, BlockPattern.WhiteSquare)
        self.assertEqual(block.getPattern(), BlockPattern.White)

    def test_random_search_puzzle(self):
        expected_patterns = [
            BlockPattern.BlackSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackSquare
        ]
        puzzle = Puzzle([
            BlockPattern.BlackSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackSquare
        ], random_search)
        puzzle.solve()
        actual_patterns = []
        for block in puzzle.blockBank:
            actual_patterns.append(block.getPattern())
        self.assertEqual(actual_patterns, expected_patterns)            
        
if __name__ == '__main__':
    unittest.main()
