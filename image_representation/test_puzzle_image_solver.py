import unittest
import numpy as np
from utils.enums import BlockPattern
from puzzle_image_solver import PuzzleImageSolver, SearchType, random_search, sequential_search

class TestPuzzleImageSolver(unittest.TestCase):

    def test_init(self):
        print('\nInstantiates a puzzle image')
        puzzle_solver = PuzzleImageSolver('./puzzle_images/puzzle_a.png')
        img = puzzle_solver.getImage()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue((img[100][103] == [27, 13, 252]).all()) # Shaded
        self.assertTrue((img[0][0] == [255, 255, 255]).all()) # White

    def test_top_right(self):
        puzzle_solver = PuzzleImageSolver('./face_images/top_right.png')
        self.assertEqual(puzzle_solver.getPattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_bottom_right(self):
        puzzle_solver = PuzzleImageSolver('./face_images/bottom_right.png')
        self.assertEqual(puzzle_solver.getPattern(), BlockPattern.BlackBottomRightCornerSquare)

    def test_bottom_left(self):
        puzzle_solver = PuzzleImageSolver('./face_images/bottom_left.png')
        self.assertEqual(puzzle_solver.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_top_left(self):
        puzzle_solver = PuzzleImageSolver('./face_images/top_left.png')
        self.assertEqual(puzzle_solver.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_white(self):
        puzzle_solver = PuzzleImageSolver('./face_images/white.png')
        self.assertEqual(puzzle_solver.getPattern(), BlockPattern.WhiteSquare)

    def test_shaded(self):
        puzzle_solver = PuzzleImageSolver('./face_images/shaded.png')
        self.assertEqual(puzzle_solver.getPattern(), BlockPattern.BlackSquare)

    def test_puzzle_a(self):
        puzzle_solver = PuzzleImageSolver('./puzzle_images/puzzle_a.png')
        actual = puzzle_solver.getPuzzle()
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
        puzzle_solver = PuzzleImageSolver('./puzzle_images/puzzle_b.png')
        actual = puzzle_solver.getPuzzle()
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
        puzzle_solver = PuzzleImageSolver('./puzzle_images/puzzle_c.png')
        actual = puzzle_solver.getPuzzle()
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
        print('\nInstantiates a block bank with correct length')
        puzzle_solver = PuzzleImageSolver('./puzzle_images/puzzle_c.png')
        self.assertEqual(len(puzzle_solver.blockBank), 9)

    # def test_random_search(self):
    #     print('\nApply random search for a single block')
    #     block = Block(1, 1)
    #     self.assertEqual(block.getFace(), 1)
    #     self.assertEqual(block.getPattern(),
    #                      BlockPattern.BlackTopRightCornerSquare)
    #     random_search(block, BlockPattern.WhiteSquare, [])
    #     self.assertEqual(block.getPattern(), BlockPattern.WhiteSquare)

    # def test_random_search_puzzle(self):
    #     print('\nApply random search for the puzzle')
    #     expected_patterns = [
    #         BlockPattern.BlackSquare,
    #         BlockPattern.BlackBottomLeftCornerSquare,
    #         BlockPattern.BlackTopRightCornerSquare,
    #         BlockPattern.BlackSquare
    #     ]
    #     puzzle_solver = PuzzleSolver([
    #         BlockPattern.BlackSquare,
    #         BlockPattern.BlackBottomLeftCornerSquare,
    #         BlockPattern.BlackTopRightCornerSquare,
    #         BlockPattern.BlackSquare
    #     ], {
    #         SearchType.Face: random_search,
    #         SearchType.PuzzlePiece: sequential_search
    #     })
    #     puzzle_solver.solve()
    #     actual_patterns = []
    #     for block in puzzle_solver.blockBank:
    #         actual_patterns.append(block.getPattern())
    #     self.assertEqual(actual_patterns, expected_patterns)            

if __name__ == '__main__':
    unittest.main()
