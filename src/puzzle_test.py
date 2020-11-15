import unittest

from block import BlockPattern, Block
from puzzle import Puzzle, SearchType, random_search, sequential_search

class TestPuzzle(unittest.TestCase):

    def test_init(self):
        print('\nInstantiates a block bank with correct length')
        puzzle = Puzzle([
            BlockPattern.BlackSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackSquare
        ], {
            SearchType.Face: random_search,
            SearchType.PuzzlePiece: sequential_search
        })
        self.assertEqual(len(puzzle.blockBank), 4)

    def test_random_search(self):
        print('\nApply random search for a single block')
        block = Block(1, 1)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(),
                         BlockPattern.BlackTopRightCornerSquare)
        random_search(block, BlockPattern.WhiteSquare, [])
        self.assertEqual(block.getPattern(), BlockPattern.WhiteSquare)

    def test_random_search_puzzle(self):
        print('\nApply random search for the puzzle')
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
        ], {
            SearchType.Face: random_search,
            SearchType.PuzzlePiece: sequential_search
        })
        puzzle.solve()
        actual_patterns = []
        for block in puzzle.blockBank:
            actual_patterns.append(block.getPattern())
        self.assertEqual(actual_patterns, expected_patterns)            
        
if __name__ == '__main__':
    unittest.main()
