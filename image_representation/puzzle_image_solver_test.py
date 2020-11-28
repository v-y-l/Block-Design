import unittest
import numpy as np
from utils.enums import BlockPattern
from puzzle_image_solver import PuzzleImageSolver

class TestPuzzleImageSolver(unittest.TestCase):

    def test_init(self):
        print('\nInstantiates a puzzle image')
        puzzle_image = PuzzleImageSolver('./puzzle_images/puzzle_a.png')
        img = puzzle_image.getImage()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue((img[100][103] == [27, 13, 252]).all()) # Shaded
        self.assertTrue((img[0][0] == [255, 255, 255]).all()) # White

    def test_top_right(self):
        puzzle_image = PuzzleImageSolver('./face_images/top_right.png')
        self.assertEqual(puzzle_image.getPattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_bottom_right(self):
        puzzle_image = PuzzleImageSolver('./face_images/bottom_right.png')
        self.assertEqual(puzzle_image.getPattern(), BlockPattern.BlackBottomRightCornerSquare)

    def test_bottom_left(self):
        puzzle_image = PuzzleImageSolver('./face_images/bottom_left.png')
        self.assertEqual(puzzle_image.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_top_left(self):
        puzzle_image = PuzzleImageSolver('./face_images/top_left.png')
        self.assertEqual(puzzle_image.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_white(self):
        puzzle_image = PuzzleImageSolver('./face_images/white.png')
        self.assertEqual(puzzle_image.getPattern(), BlockPattern.WhiteSquare)

    def test_shaded(self):
        puzzle_image = PuzzleImageSolver('./face_images/shaded.png')
        self.assertEqual(puzzle_image.getPattern(), BlockPattern.BlackSquare)

    def test_puzzle_a(self):
        puzzle_image = PuzzleImageSolver('./puzzle_images/puzzle_a.png')
        actual = puzzle_image.getPuzzle()
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
        puzzle_image = PuzzleImageSolver('./puzzle_images/puzzle_b.png')
        actual = puzzle_image.getPuzzle()
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
        puzzle_image = PuzzleImageSolver('./puzzle_images/puzzle_c.png')
        actual = puzzle_image.getPuzzle()
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

if __name__ == '__main__':
    unittest.main()
