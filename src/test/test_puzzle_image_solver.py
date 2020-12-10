import unittest
import numpy as np
from utils.enums import BlockPattern
from block_image import BlockImage
from search import random_search, sequential_search, beeline_search
from puzzle_image_solver import PuzzleImageSolver, SearchType

class TestPuzzleImageSolver(unittest.TestCase):

    def test_init(self):
        print('Instantiates puzzle a image')
        puzzle_solver = PuzzleImageSolver('puzzle_a')
        img = puzzle_solver.get_image()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue((img[100][103] == [27, 13, 252]).all()) # Shaded
        self.assertTrue((img[0][0] == [255, 255, 255]).all()) # White

    def test_top_right(self):
        print('Instantiates top right image')
        puzzle_solver = PuzzleImageSolver('top_right')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackTopRightCornerSquare)

    def test_bottom_right(self):
        print('Instantiates bottom right image')
        puzzle_solver = PuzzleImageSolver('bottom_right')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackBottomRightCornerSquare)

    def test_bottom_left(self):
        print('Instantiates bottom left image')
        puzzle_solver = PuzzleImageSolver('bottom_left')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackBottomLeftCornerSquare)

    def test_top_left(self):
        print('Instantiates top left image')
        puzzle_solver = PuzzleImageSolver('top_left')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackTopLeftCornerSquare)

    def test_white(self):
        print('Instantiates white image')
        puzzle_solver = PuzzleImageSolver('white')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.WhiteSquare)

    def test_shaded(self):
        print('Instantiates shaded image')
        puzzle_solver = PuzzleImageSolver('shaded')
        self.assertEqual(puzzle_solver.get_pattern(0, 0), BlockPattern.BlackSquare)

    def test_puzzle_a(self):
        print('Instantiates puzzle a image')
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
        print('Instantiates puzzle b image')
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
        print('Instantiates puzzle c image')
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
        print('Instantiates block bank with correct length')
        puzzle_solver = PuzzleImageSolver('puzzle_c')
        self.assertEqual(len(puzzle_solver.block_bank), 9)

    def test_random_search(self):
        print('Apply random search for a single block')
        block = BlockImage(1, 1)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(),
                         BlockPattern.BlackTopRightCornerSquare)
        random_search(block, BlockPattern.WhiteSquare, [])
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)

    def test_random_search_puzzle(self):
        print('Random search for puzzle c')
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
            'puzzle_memory_loss_factor': 0,
            'puzzle_memory_loss_counter_limit': 0
        })
        puzzle_solver.solve()
        actual_patterns = []
        for pieces in sorted(puzzle_solver.solved_pieces):
            block = puzzle_solver.solved_pieces[pieces]
            actual_patterns.append(block.get_pattern())
        self.assertEqual(actual_patterns, expected_patterns)

    def test_memory_loss_puzzle(self):
        print('Beeline search with memory loss on puzzle c')
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
                SearchType.Face: beeline_search,
                SearchType.PuzzlePiece: sequential_search
            },
            'puzzle_memory_loss_factor': .5,
            'puzzle_memory_loss_counter_limit': 3
        })
        puzzle_solver.solve()
        actual_patterns = []
        for pieces in sorted(puzzle_solver.solved_pieces):
            block = puzzle_solver.solved_pieces[pieces]
            actual_patterns.append(block.get_pattern())
        self.assertEqual(actual_patterns, expected_patterns)
        self.assertTrue(len(puzzle_solver.action_history) >= 27)

if __name__ == '__main__':
    unittest.main()
