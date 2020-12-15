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

    def test_glance_factor_puzzle_b(self):
        print('\nTests glance factor on puzzle b')
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
                'puzzle_memory_loss_factor': 1.0,
                'puzzle_memory_loss_counter_limit': 1,
                'glance_factor': .25
            })
        puzzle_solver.solve()
        actual_patterns = puzzle_solver.get_solved_pieces_patterns()
        self.assertEqual(actual_patterns, expected_patterns)
        # Would need to look up each of the 16 pieces
        self.assertEqual(len(puzzle_solver.action_history), 49)

if __name__ == '__main__':
    unittest.main()
