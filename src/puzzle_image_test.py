import unittest
from utils.enums import BlockPattern

import numpy as np
from puzzle_image import PuzzleImage

class TestPuzzleImage(unittest.TestCase):

    def test_init(self):
        print('\nInstantiates a puzzle image')
        puzzle = PuzzleImage('./puzzle_images/puzzle_a.png')
        img = puzzle.getImage()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue((img[100][103] == [27, 13, 252]).all()) # Shaded
        self.assertTrue((img[0][0] == [255, 255, 255]).all()) # White

    def test_top_right(self):
        puzzle = PuzzleImage('./face_images/top_right.png')
        self.assertEqual(puzzle.getPattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_bottom_right(self):
        puzzle = PuzzleImage('./face_images/bottom_right.png')
        self.assertEqual(puzzle.getPattern(), BlockPattern.BlackBottomRightCornerSquare)

    def test_bottom_left(self):
        puzzle = PuzzleImage('./face_images/bottom_left.png')
        self.assertEqual(puzzle.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_top_left(self):
        puzzle = PuzzleImage('./face_images/top_left.png')
        self.assertEqual(puzzle.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_white(self):
        puzzle = PuzzleImage('./face_images/white.png')
        self.assertEqual(puzzle.getPattern(), BlockPattern.WhiteSquare)

    def test_shaded(self):
        puzzle = PuzzleImage('./face_images/shaded.png')
        self.assertEqual(puzzle.getPattern(), BlockPattern.BlackSquare)

if __name__ == '__main__':
    unittest.main()
