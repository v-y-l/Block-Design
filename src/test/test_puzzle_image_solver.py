import unittest
import numpy as np
from utils.enums import BlockPattern
from block_image import BlockImage
from puzzle_image_solver import PuzzleImageSolver, SearchType, random_search, sequential_search

class TestPuzzleImageSolver(unittest.TestCase):

    def test_init(self):
        print('\n Instantiates a puzzle image')
        puzzle_solver = PuzzleImageSolver('puzzle_a')
        img = puzzle_solver.get_image()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue((img[100][103] == [27, 13, 252]).all()) # Shaded
        self.assertTrue((img[0][0] == [255, 255, 255]).all()) # White

    def test_top_right(self):
        puzzle_solver = PuzzleImageSolver('top_right')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackTopRightCornerSquare)

    def test_bottom_right(self):
        puzzle_solver = PuzzleImageSolver('bottom_right')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackBottomRightCornerSquare)

    def test_bottom_left(self):
        puzzle_solver = PuzzleImageSolver('bottom_left')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackBottomLeftCornerSquare)

    def test_top_left(self):
        puzzle_solver = PuzzleImageSolver('top_left')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackTopLeftCornerSquare)

    def test_white(self):
        puzzle_solver = PuzzleImageSolver('white')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.WhiteSquare)

    def test_shaded(self):
        puzzle_solver = PuzzleImageSolver('shaded')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackSquare)

    def test_puzzle_a(self):
        puzzle_solver = PuzzleImageSolver('puzzle_a')
        actual = puzzle_solver.get_puzzle()
        expected = [
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare
        ]
        self.assertEqual(actual, expected)

    def test_puzzle_b(self):
        puzzle_solver = PuzzleImageSolver('puzzle_b')
        actual = puzzle_solver.get_puzzle()
        expected = [
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
        ]
        self.assertEqual(actual, expected)

    def test_puzzle_c(self):
        puzzle_solver = PuzzleImageSolver('puzzle_c')
        actual = puzzle_solver.get_puzzle()
        expected = [
            BlockPattern.WhiteSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.WhiteSquare,
            BlockPattern.WhiteSquare,
            BlockPattern.WhiteSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackBottomRightCornerSquare,
        ]
        self.assertEqual(actual, expected)

    def test_block_bank(self):
        print('\n Instantiates a block bank with correct length')
        puzzle_solver = PuzzleImageSolver('puzzle_c')
        self.assertEqual(len(puzzle_solver.block_bank), 9)

    def test_random_search(self):
        print('\nApply random search for a single block')
        block = BlockImage(1, 1)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(),
                         BlockPattern.BlackTopRightCornerSquare)
        random_search(block, BlockPattern.WhiteSquare, [])
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)

    def test_random_search_puzzle(self):
        print('\n Apply random search for the puzzle')
        expected_patterns = [
            BlockPattern.WhiteSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.WhiteSquare,
            BlockPattern.WhiteSquare,
            BlockPattern.WhiteSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackBottomRightCornerSquare,
        ]
        puzzle_solver = PuzzleImageSolver(
            'puzzle_c', {
            'solvers': {
                SearchType.Face: random_search,
                SearchType.PuzzlePiece: sequential_search
            },
            'puzzle_memory_loss_factor': 0
        })
        puzzle_solver.solve()
        actual_patterns = []
        for pieces in sorted(puzzle_solver.solved_pieces):
            block = puzzle_solver.solved_pieces[pieces]
            actual_patterns.append(block.get_pattern())
        self.assertEqual(actual_patterns, expected_patterns)

if __name__ == '__main__':
    unittest.main()
