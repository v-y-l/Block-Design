import unittest
import numpy as np
from utils.enums import BlockPattern
from block_image import BlockImage
from search import random_search, sequential_search, beeline_search
from puzzle_image_solver import PuzzleImageSolver, SearchType

class TestPuzzleImageSolver(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n\nPUZZLE IMAGE SOLVER TESTS')

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

    def test_random_search_puzzle_c(self):
        print('\nTests random search for puzzle c')
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
            'puzzle_memory_loss_counter_limit': 0,
            'glance_factor': 1.0
        })
        puzzle_solver.solve()
        actual_patterns = []
        for pieces in sorted(puzzle_solver.solved_pieces):
            block = puzzle_solver.solved_pieces[pieces]
            actual_patterns.append(block.get_pattern())
        self.assertEqual(actual_patterns, expected_patterns)

    def test_beeline_search_puzzle_b(self):
        print('\nTests beeline search on puzzle b')
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
        puzzle_solver = PuzzleImageSolver(
            'puzzle_b', {
                'solvers': {
                    SearchType.Face: beeline_search,
                    SearchType.PuzzlePiece: sequential_search
                },
                'puzzle_memory_loss_factor': 0.0,
                'puzzle_memory_loss_counter_limit': 0,
                'glance_factor': 1.0
            })
        puzzle_solver.solve()
        actual_patterns = puzzle_solver.get_solved_pieces_patterns()
        self.assertEqual(actual_patterns, expected_patterns)
        self.assertEqual(len(puzzle_solver.action_history), 33)

    def test_memory_loss_puzzle_b(self):
        print('\nTests beeline search with memory loss on puzzle b')
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
        puzzle_solver = PuzzleImageSolver(
            'puzzle_b', {
            'solvers': {
                SearchType.Face: beeline_search,
                SearchType.PuzzlePiece: sequential_search
            },
            'puzzle_memory_loss_factor': .5,
            'puzzle_memory_loss_counter_limit': 3,
            'glance_factor': 1.0
        })
        puzzle_solver.solve()
        actual_patterns = puzzle_solver.get_solved_pieces_patterns()
        self.assertEqual(actual_patterns, expected_patterns)

    def test_memory_loss_puzzle_c(self):
        print('\nTests beeline search with memory loss on puzzle c')
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
            'puzzle_memory_loss_counter_limit': 3,
            'glance_factor': 1.0
        })
        puzzle_solver.solve()
        actual_patterns = puzzle_solver.get_solved_pieces_patterns()
        self.assertEqual(actual_patterns, expected_patterns)

if __name__ == '__main__':
    unittest.main()
