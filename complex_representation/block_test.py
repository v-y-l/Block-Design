import unittest

from block import Block, BlockPattern

class TestBlockMethods(unittest.TestCase):

    def test_gotoface(self):
        block = Block()
        self.assertEqual(block.current_face, 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        block.goToFace(4)
        self.assertEqual(block.current_face, 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(5)
        self.assertEqual(block.current_face, 5)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(1)
        self.assertEqual(block.current_face, 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_rotations(self):
        block = Block()
        self.assertEqual(block.current_face, 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        block.rotateRight()
        self.assertEqual(block.current_face, 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomRightCornerSquare)
        block.goToFace(4)
        self.assertEqual(block.current_face, 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(6)
        self.assertEqual(block.current_face, 6)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

if __name__ == '__main__':
    unittest.main()
