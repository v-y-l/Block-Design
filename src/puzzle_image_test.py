import unittest

import numpy as np
from puzzle_image import PuzzleImage

class TestPuzzleImage(unittest.TestCase):

    def test_init(self):
        print('\nInstantiates a puzzle image')
        puzzle = PuzzleImage('./puzzle_images/puzzle_a.png')
        img = puzzle.getImage()
        self.assertEqual(img.shape, (680,680,3))
        # B, G, R
        self.assertTrue(np.all(img[100][103] - [27, 13, 252] == 0)) # Shaded
        self.assertTrue(np.all(img[0][0] - [255, 255, 255] == 0)) # White

if __name__ == '__main__':
    unittest.main()
