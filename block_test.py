import unittest

from block import Block, BlockOrientation

class TestBlockMethods(unittest.TestCase):

    def test_flipdown(self):
        block = Block()
        self.assertEqual(block.face[1], BlockOrientation.Up)
        self.assertEqual(block.face[0], 1)
        block.flipDown()
        self.assertEqual(block.face[1], BlockOrientation.Up)
        self.assertEqual(block.face[0], 5)
        block.flipDown()
        self.assertEqual(block.face[1], BlockOrientation.Up)
        self.assertEqual(block.face[0], 6)
        block.flipDown()
        self.assertEqual(block.face[1], BlockOrientation.Up)
        self.assertEqual(block.face[0], 3)


    def test_flipright(self):
        block = Block()
        self.assertEqual(block.face[1], BlockOrientation.Up)
        self.assertEqual(block.face[0], 1)
        block.flipRight()
        self.assertEqual(block.face[1], BlockOrientation.Right)
        self.assertEqual(block.face[0], 2)
        block.flipRight()
        self.assertEqual(block.face[1], BlockOrientation.Down)
        self.assertEqual(block.face[0], 6)
        block.flipRight()
        self.assertEqual(block.face[1], BlockOrientation.Left)
        self.assertEqual(block.face[0], 4)

    def test_flipsequenceone(self):
        block = Block()
        self.assertEqual(block.face[1], BlockOrientation.Up)
        self.assertEqual(block.face[0], 1)
        block.flipLeft()
        self.assertEqual(block.face[1], BlockOrientation.Right)
        self.assertEqual(block.face[0], 4)
        block.flipDown()
        self.assertEqual(block.face[1], BlockOrientation.Left)
        self.assertEqual(block.face[0], 5)
        block.flipRight()
        self.assertEqual(block.face[0], 1)

if __name__ == '__main__':
    unittest.main()
