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


if __name__ == '__main__':
    unittest.main()
