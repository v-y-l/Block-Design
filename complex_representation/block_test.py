import unittest

from block import Block, BlockPattern

class TestBlockMethods(unittest.TestCase):

    def test_sequenceone(self):
        block = Block()
        self.assertEqual(block.current_face, 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        block.goToFace(4)
        self.assertEqual(block.face[0], 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(5)
        self.assertEqual(block.face[0], 5)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        block.goToFace(1)
        self.assertEqual(block.face[0], 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

if __name__ == '__main__':
    unittest.main()
