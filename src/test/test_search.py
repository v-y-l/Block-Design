import unittest

from block_image import BlockPattern, BlockImage
from search import memory_search, random_search, beeline_search, sequential_search, skip_unknown_search
from puzzle_image_solver import PuzzleImageSolver, SearchType, PuzzleAction

class TestSearchMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n\nSEARCH TESTS')

    def test_memory_search(self):
        print('\nTests memory search')
        actions = memory_search(BlockImage(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage()
        visited = [(block.get_face(), block.get_pattern())]
        for action in actions:
            block.execute_action(action)
            visited.append((block.get_face(), block.get_pattern()))
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopLeftCornerSquare)
        self.assertEqual(len(visited), len(set(visited)))

    def test_random_search(self):
        print('\nTests random search')
        actions = random_search(BlockImage(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage()
        for action in actions:
            block.execute_action(action)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_beeline_search_rotations(self):
        print('\nTests beeline search, rotations')
        actions = beeline_search(BlockImage(), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage()
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)
        self.assertEqual(len(actions), 1)
        block.execute_action(actions[0])
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopLeftCornerSquare)

        actions = beeline_search(BlockImage(), BlockPattern.BlackBottomLeftCornerSquare, [])
        block = BlockImage()
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopRightCornerSquare)
        # Since beeline search is somewhat stochastic, these test rely on heuristics
        self.assertEqual(len(actions), 2)
        for action in actions:
            block.execute_action(action)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackBottomLeftCornerSquare)

    def test_beeline_search_complex(self):
        print('\nTests beeline search, complex sequence')
        actions = beeline_search(BlockImage(3), BlockPattern.BlackTopLeftCornerSquare, [])
        block = BlockImage(3)
        self.assertEqual(block.get_pattern(), BlockPattern.WhiteSquare)
        self.assertTrue(len(actions) == 2)
        for action in actions:
             block.execute_action(action)
        self.assertEqual(block.get_pattern(), BlockPattern.BlackTopLeftCornerSquare)

    def test_sequential_search(self):
        print('\nTests sequential search')
        expected_patterns = [
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
        ]
        puzzle_solver = PuzzleImageSolver(
            'puzzle_b', {
                'solvers': {
                    SearchType.Face: beeline_search,
                    SearchType.PuzzlePiece: sequential_search
                },
                'puzzle_memory_loss_factor': 0.0,
                'puzzle_memory_loss_counter_limit': 0,
                'glance_factor': .25
            })
        puzzle_solver.solve()
        actual_patterns = puzzle_solver.get_solved_pieces_patterns()
        self.assertEqual(actual_patterns, expected_patterns)
        self.assertEqual(
            puzzle_solver.action_counter[PuzzleAction.LookAtPuzzle],
            16
        )

    def test_skip_unknown_search(self):
        print('\nTests skip unknown search')
        expected_patterns = [
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
            BlockPattern.BlackSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackTopLeftCornerSquare,
            BlockPattern.BlackTopRightCornerSquare,
            BlockPattern.BlackBottomLeftCornerSquare,
            BlockPattern.BlackBottomRightCornerSquare,
        ]
        puzzle_solver = PuzzleImageSolver(
            'puzzle_b', {
                'solvers': {
                    SearchType.Face: beeline_search,
                    SearchType.PuzzlePiece: skip_unknown_search
                },
                'puzzle_memory_loss_factor': 0.0,
                'puzzle_memory_loss_counter_limit': 0,
                'glance_factor': .5
            })
        puzzle_solver.solve()
        actual_patterns = puzzle_solver.get_solved_pieces_patterns()
        self.assertEqual(actual_patterns, expected_patterns)
        self.assertEqual(puzzle_solver.action_counter[PuzzleAction.LookAtPuzzle], 4)

if __name__ == '__main__':
    unittest.main()
