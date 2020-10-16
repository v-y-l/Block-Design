import unittest

from block import Pattern
from puzzle import Puzzle

class TestBlockMethods(unittest.TestCase):

    def test_init(self):
        puzzle = Puzzle(
            [Pattern.Triangle, Pattern.Triangle, Pattern.Triangle, Pattern.Triangle])
        self.assertEqual(len(puzzle.blocks), 4)
        
if __name__ == '__main__':
    unittest.main()
