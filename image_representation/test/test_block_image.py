import unittest

from block_image import BlockImage, BlockPattern, BlockAction

class TestBlockImageMethods(unittest.TestCase):

    def test_simple_sequence_one(self):
        print('\nSimple sequence one')
        block = BlockImage()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        
        block.executeAction(BlockAction.GoToFaceFour)
        self.assertEqual(block.getFace(), 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        
        block.executeAction(BlockAction.GoToFaceFive)
        self.assertEqual(block.getFace(), 5)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        
        block.executeAction(BlockAction.GoToFaceOne)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_simple_sequence_two(self):
        print('\nSimple sequence two')
        block = BlockImage()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        
        block.executeAction(BlockAction.RotateRight)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomRightCornerSquare)
        
        block.executeAction(BlockAction.GoToFaceFour)
        self.assertEqual(block.getFace(), 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        
        block.executeAction(BlockAction.GoToFaceSix)
        self.assertEqual(block.getFace(), 6)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_complex_sequence(self):
        print('\Complex sequence')
        block = BlockImage()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)
        
        block.executeAction(BlockAction.GoToFaceFour)
        self.assertEqual(block.getFace(), 4)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        
        block.executeAction(BlockAction.GoToFaceThree)
        self.assertEqual(block.getFace(), 3)
        self.assertEqual(block.getPattern(), BlockPattern.WhiteSquare)
        
        block.executeAction(BlockAction.RotateRight)
        self.assertEqual(block.getFace(), 3)
        self.assertEqual(block.getPattern(), BlockPattern.WhiteSquare)
        
        block.executeAction(BlockAction.GoToFaceOne)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomRightCornerSquare)
        
        block.executeAction(BlockAction.GoToFaceFive)
        self.assertEqual(block.getFace(), 5)
        self.assertEqual(block.getPattern(), BlockPattern.BlackSquare)
        
        block.executeAction(BlockAction.GoToFaceSix)
        self.assertEqual(block.getFace(), 6)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)
        
        block.executeAction(BlockAction.RotateRight)
        self.assertEqual(block.getFace(), 6)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopLeftCornerSquare)
        
        block.executeAction(BlockAction.GoToFaceThree)
        self.assertEqual(block.getFace(), 3)
        self.assertEqual(block.getPattern(), BlockPattern.WhiteSquare)
        
        block.executeAction(BlockAction.GoToFaceOne)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomLeftCornerSquare)
        
        block.executeAction(BlockAction.RotateLeft)
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomRightCornerSquare)

    def test_invalid_sequence(self):
        print('\Invalid sequence should not be possible')
        block = BlockImage()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), BlockPattern.BlackTopRightCornerSquare)

        with self.assertRaises(Exception) as context:
            block.executeAction(BlockAction.GoToFaceSix)
        self.assertEqual(str(context.exception), "Can't go from 1 to 6")

    def test_peek(self):
        print('\Test peek')
        block = BlockImage(6)
        self.assertEqual(block.getPattern(), BlockPattern.BlackBottomRightCornerSquare)
        self.assertEqual(block.peekAction(BlockAction.RotateRight),
            BlockPattern.BlackBottomLeftCornerSquare)
        self.assertEqual(block.peekAction(BlockAction.RotateLeft),
            BlockPattern.BlackTopRightCornerSquare)
        self.assertEqual(block.peekAction(BlockAction.GoToFaceThree),
            BlockPattern.WhiteSquare)
        with self.assertRaises(Exception) as context:
            block.peekAction(BlockAction.GoToFaceOne)
        self.assertEqual(str(context.exception),
                         "Invalid action BlockAction.GoToFaceOne for Block 1: " +
                         "face 6, pattern BlockPattern.BlackBottomRightCornerSquare")

if __name__ == '__main__':
    unittest.main()