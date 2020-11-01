import unittest

from block import Block, BlockPattern

class TestBlockMethods(unittest.TestCase):

    def test_gotoface(self):
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


    def test_gotofaceexception(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

        with self.assertRaises(Exception) as context:
            block.goToFace(6)
        self.assertEqual(str(context.exception), "Can't go from 1 to 6")

    def test_rotations(self):
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

if __name__ == '__main__':
    unittest.main()
