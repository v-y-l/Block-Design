import unittest
from results_analyzer import ResultsAnalyzer

class TestResultsAnalyzerMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n\nANALYZER TESTS')

    def test_small_run_analysis(self):
        print('\nTests small run')
        analyzer = ResultsAnalyzer("past_runs/test_run.csv", None, True)
        analyzer.analyze()
        self.assertEqual(analyzer.metadata["num_pieces"], 9)
        self.assertEqual(analyzer.stats["num_runs"], 3)
        self.assertEqual(analyzer.stats["min_actions"], 19)
        self.assertEqual(analyzer.stats["mean_actions"], 19)
        self.assertEqual(analyzer.stats["max_actions"], 19)
        self.assertEqual(analyzer.stats["mean_actions_per_block"], 1.89)
        self.assertEqual(analyzer.stats["min_look_at_puzzle_actions"], 2)
        self.assertEqual(analyzer.stats["mean_look_at_puzzle_actions"], 2)
        self.assertEqual(analyzer.stats["max_look_at_puzzle_actions"], 2)
        self.assertEqual(analyzer.stats["std_dev_actions"], 0)
        self.assertEqual(analyzer.stats["std_dev_look_at_puzzle_actions"],
                         0)

    def test_medium_run_analysis(self):
        print('\nTests medium run')
        analyzer = ResultsAnalyzer("past_runs/test_medium_run.csv",
                                   None, True)
        analyzer.analyze()
        self.assertEqual(analyzer.metadata["num_pieces"], 16)
        self.assertEqual(analyzer.stats["num_runs"], 3)
        self.assertEqual(analyzer.stats["min_actions"], 19)
        self.assertEqual(analyzer.stats["mean_actions"], 19)
        self.assertEqual(analyzer.stats["max_actions"], 19)
        self.assertEqual(analyzer.stats["mean_actions_per_block"], 1.89)
        self.assertEqual(analyzer.stats["min_look_at_puzzle_actions"], 2)
        self.assertEqual(analyzer.stats["mean_look_at_puzzle_actions"], 2)
        self.assertEqual(analyzer.stats["max_look_at_puzzle_actions"], 2)
        self.assertEqual(analyzer.stats["std_dev_actions"], 0)
        self.assertEqual(analyzer.stats["std_dev_look_at_puzzle_actions"],
                         0)
