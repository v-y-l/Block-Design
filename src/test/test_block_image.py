import unittest

from block_image import BlockImage, BlockPattern, BlockAction

class TestBlockImageMethods(unittest.TestCase):

    def test_simple_sequence_one(self):
        print('\n Simple sequence one')
        block = BlockImage()
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)
        
        block.execute_action(BlockAction.GoToFaceFour)
        self.assertEqual(block.get_face(), 4)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackSquare)
        
        block.execute_action(BlockAction.GoToFaceFive)
        self.assertEqual(block.get_face(), 5)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackSquare)
        
        block.execute_action(BlockAction.GoToFaceOne)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)

    def test_simple_sequence_two(self):
        print('\n Simple sequence two')
        block = BlockImage()
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)
        
        block.execute_action(BlockAction.RotateRight)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomRightCornerSquare)
        
        block.execute_action(BlockAction.GoToFaceFour)
        self.assertEqual(block.get_face(), 4)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackSquare)
        
        block.execute_action(BlockAction.GoToFaceSix)
        self.assertEqual(block.get_face(), 6)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_complex_sequence(self):
        print('\n Complex sequence')
        block = BlockImage()
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)
        
        block.execute_action(BlockAction.GoToFaceFour)
        self.assertEqual(block.get_face(), 4)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackSquare)
        
        block.execute_action(BlockAction.GoToFaceThree)
        self.assertEqual(block.get_face(), 3)
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)
        
        block.execute_action(BlockAction.RotateRight)
        self.assertEqual(block.get_face(), 3)
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)
        
        block.execute_action(BlockAction.GoToFaceOne)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomRightCornerSquare)
        
        block.execute_action(BlockAction.GoToFaceFive)
        self.assertEqual(block.get_face(), 5)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackSquare)
        
        block.execute_action(BlockAction.GoToFaceSix)
        self.assertEqual(block.get_face(), 6)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomLeftCornerSquare)
        
        block.execute_action(BlockAction.RotateRight)
        self.assertEqual(block.get_face(), 6)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopLeftCornerSquare)
        
        block.execute_action(BlockAction.GoToFaceThree)
        self.assertEqual(block.get_face(), 3)
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)
        
        block.execute_action(BlockAction.GoToFaceOne)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomLeftCornerSquare)
        
        block.execute_action(BlockAction.RotateLeft)
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomRightCornerSquare)

    def test_invalid_sequence(self):
        print('\n Invalid sequence should not be possible')
        block = BlockImage()
        self.assertEqual(block.get_face(), 1)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)

        with self.assertRaises(Exception) as context:
            block.execute_action(BlockAction.GoToFaceSix)
        self.assertEqual(str(context.exception), "Can't go from 1 to 6")

    def test_peek(self):
        print('\n Test peek')
        block = BlockImage(6)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomRightCornerSquare)
        self.assertEqual(block.peek_action(BlockAction.RotateRight),
            BlockPattern.BlackBottomLeftCornerSquare)
        self.assertEqual(block.peek_action(BlockAction.RotateLeft),
            BlockPattern.BlackTopRightCornerSquare)
        self.assertEqual(block.peek_action(BlockAction.GoToFaceThree),
            BlockPattern.WhiteSquare)
        with self.assertRaises(Exception) as context:
            block.peek_action(BlockAction.GoToFaceOne)
        self.assertEqual(str(context.exception),
                         "Invalid action BlockAction.GoToFaceOne for " +
                         "Block,1,Face,6,Pattern,BlackBottomRightCornerSquare")

if __name__ == '__main__':
    unittest.main()
