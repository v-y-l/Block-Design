import unittest

from block_image import BlockPattern, BlockImage
from search import random_search, beeline_search

class TestSearchMethods(unittest.TestCase):

    def test_random_search(self):
        print('\nRandom search')
        actions = random_search(BlockImage(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage()
        for action in actions:
            block.executeAction(action)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_beeline_search_rotations(self):
        print('\Beeline search - rotations')
        actions = beeline_search(BlockImage(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage()
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        self.assertEqual(len(actions), 1)
        block.executeAction(actions[0])
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

        actions = beeline_search(BlockImage(), BlockPattern.BlackBottomLeftCornerSquare, [])
        block = BlockImage()
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        # Since beeline search is somewhat stochastic, these test rely on heuristics
        self.assertEqual(len(actions), 2)
        for action in actions:
            block.executeAction(action)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_beeline_search_complex(self):
        print('\Beeline search - complex')
        actions = beeline_search(BlockImage(3), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage(3)
        self.assertEqual(block.getPattern(), BlockPattern.WhiteSquare)
        self.assertTrue(len(actions) == 2)
        for action in actions:
             block.executeAction(action)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)

if __name__ == '__main__':
    unittest.main()
