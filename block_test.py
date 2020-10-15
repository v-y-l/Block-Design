import unittest

from block import Block

class TestBlockMethods(unittest.TestCase):

    def test_flipright(self):
        block = Block()
        self.assertEqual(block.face[0], 1)
        block.flipRight()
        self.assertEqual(block.face[0], 2)
        block.flipRight()
        self.assertEqual(block.face[0], 6)
        block.flipRight()
        self.assertEqual(block.face[0], 4)


if __name__ == '__main__':
    unittest.main()
