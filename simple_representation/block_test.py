import unittest

from block import Block, Pattern

class TestBlockMethods(unittest.TestCase):

    def test_valid_sequence(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), Pattern.Triangle)

if __name__ == '__main__':
    unittest.main()
