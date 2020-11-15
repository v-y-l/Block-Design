import unittest

from puzzle_image import PuzzleImage

class TestPuzzleImage(unittest.TestCase):

    def test_init(self):
        print('\nInstantiates a puzzle image')
        puzzle = PuzzleImage('./puzzle_images/puzzle_a.png')
        img = puzzle.getImage()
        self.assertEqual(img.shape, (680,680,3))

if __name__ == '__main__':
    unittest.main()
