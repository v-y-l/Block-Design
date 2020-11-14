import unittest

from block import BlockPattern, Block
from search import random_search

class TestSearchMethods(unittest.TestCase):

    def test_random_search(self):
        print('\nRandom search')
        actions = random_search(Block(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = Block()
        for action in actions:
            block.executeAction(action)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

if __name__ == '__main__':
    unittest.main()
