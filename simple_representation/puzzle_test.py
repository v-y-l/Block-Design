import unittest

from block import Pattern, Block
from puzzle import Puzzle, random_search

class TestBlockMethods(unittest.TestCase):

    def test_init(self):
        puzzle = Puzzle(
            [Pattern.Triangle, Pattern.Triangle, Pattern.Triangle, Pattern.Triangle],
            random_search)
        self.assertEqual(len(puzzle.blocks), 4)

    def test_random_search(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), Pattern.Triangle)
        moves = random_search(block, Pattern.White)
        for m in moves:
            block.goToFace(m)
        self.assertEqual(block.getPattern(), Pattern.White)

        
if __name__ == '__main__':
    unittest.main()
