import unittest
import numpy as np
from utils.enums import BlockPattern
from block_image import BlockImage
from search import random_search, sequential_search, beeline_search
from puzzle_image_solver import PuzzleImageSolver, SearchType

class TestBasicPuzzleImageSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n\nBASIC PUZZLE IMAGE SOLVER TESTS')

    def test_init(self):
        print('\nTests puzzle a image instantiation')
        puzzle_solver = PuzzleImageSolver('puzzle_a')
        img = puzzle_solver.get_image()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue((img[100][103] == [27, 13, 252]).all()) # Shaded
        self.assertTrue((img[0][0] == [255, 255, 255]).all()) # White

    def test_top_right(self):
        print('\nTests top right image instantiation')
        puzzle_solver = PuzzleImageSolver('top_right')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackTopRightCornerSquare)

    def test_bottom_right(self):
        print('\nTests bottom right image instantiation')
        puzzle_solver = PuzzleImageSolver('bottom_right')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackBottomRightCornerSquare)

    def test_bottom_left(self):
        print('\nTests bottom left image instantiation')
        puzzle_solver = PuzzleImageSolver('bottom_left')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackBottomLeftCornerSquare)

    def test_top_left(self):
        print('\nTests top left image instantiation')
        puzzle_solver = PuzzleImageSolver('top_left')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackTopLeftCornerSquare)

    def test_white(self):
        print('\nTests white image instantiation')
        puzzle_solver = PuzzleImageSolver('white')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.WhiteSquare)

    def test_shaded(self):
        print('\nTests shaded image instantiation')
        puzzle_solver = PuzzleImageSolver('shaded')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackSquare)

    def test_puzzle_a(self):
        print('\nTests puzzle a image instantiation')
        puzzle_solver = PuzzleImageSolver('puzzle_a')
        actual_patterns = puzzle_solver.get_puzzle()
        expected_patterns = [
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
        self.assertEqual(actual_patterns, expected_patterns)

    def test_puzzle_b(self):
        print('\nTests puzzle b image instantiation')
        puzzle_solver = PuzzleImageSolver('puzzle_b')
        actual_patterns = puzzle_solver.get_puzzle()
        expected_patterns = [
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
        self.assertEqual(actual_patterns, expected_patterns)

    def test_puzzle_c(self):
        print('\nTests puzzle c image instantiation')
        puzzle_solver = PuzzleImageSolver('puzzle_c')
        actual_patterns = puzzle_solver.get_puzzle()
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
        self.assertEqual(actual_patterns, expected_patterns)


    def test_block_bank(self):
        print('\nTests block bank instantiation')
        puzzle_solver = PuzzleImageSolver('puzzle_c')
        self.assertEqual(len(puzzle_solver.block_bank), 9)

    def test_random_search(self):
        print('\nTests random search for a single block')
        block = BlockImage(1, 1)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(),
                         BlockPattern.BlackTopRightCornerSquare)
        random_search(block, BlockPattern.WhiteSquare, [])
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)

if __name__ == '__main__':
    unittest.main()