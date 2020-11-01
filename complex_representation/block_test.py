import unittest

from block import Block, BlockPattern

class TestBlockMethods(unittest.TestCase):

    def test_simple_sequence_one(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        block.goToFace(4)
        self.assertEqual(block.getFace(), 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(5)
        self.assertEqual(block.getFace(), 5)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(1)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_simple_sequence_two(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        block.rotateRight()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomRightCornerSquare)
        block.goToFace(4)
        self.assertEqual(block.getFace(), 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(6)
        self.assertEqual(block.getFace(), 6)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_invalid_sequence(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

        with self.assertRaises(Exception) as context:
            block.goToFace(6)
        self.assertEqual(str(context.exception), "Can't go from 1 to 6")

if __name__ == '__main__':
    unittest.main()
