import unittest

from block import BlockPattern, Block
from search import random_search, beeline_search

class TestSearchMethods(unittest.TestCase):

    def test_random_search(self):
        print('\nRandom search')
        actions = random_search(Block(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = Block()
        for action in actions:
            block.executeAction(action)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_beeline_search(self):
        print('\Beeline search - rotations')
        actions = beeline_search(Block(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = Block()
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        self.assertEqual(len(actions), 1)
        block.executeAction(actions[0])
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

        actions = beeline_search(Block(), BlockPattern.BlackBottomLeftCornerSquare, [])
        block = Block()
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        # Since beeline search is somewhat stochastic, these test are heuristics
        self.assertEqual(len(actions), 2)
        for action in actions:
            block.executeAction(action)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

if __name__ == '__main__':
    unittest.main()
