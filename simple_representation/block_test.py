import unittest

from block import Block, Pattern

class TestBlockMethods(unittest.TestCase):

    def test_valid_sequence(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), Pattern.Triangle)
        block.goToFace(5)
        self.assertEqual(block.getFace(), 5)
        self.assertEqual(block.getPattern(), Pattern.Black)
        block.goToFace(2)
        self.assertEqual(block.getFace(), 2)
        self.assertEqual(block.getPattern(), Pattern.White)
        block.goToFace(3)
        self.assertEqual(block.getFace(), 3)
        self.assertEqual(block.getPattern(), Pattern.White)
        block.goToFace(4)
        self.assertEqual(block.getFace(), 4)
        self.assertEqual(block.getPattern(), Pattern.Black)
        block.goToFace(6)
        self.assertEqual(block.getFace(), 6)
        self.assertEqual(block.getPattern(), Pattern.Triangle)

    def test_invalid_sequence(self):
        block = Block()
        self.assertEqual(block.getFace(), 1)
        self.assertEqual(block.getPattern(), Pattern.Triangle)

        with self.assertRaises(Exception) as context:
            block.goToFace(6)
        self.assertEqual(str(context.exception), "Can't go from 1 to 6")
        
if __name__ == '__main__':
    unittest.main()
