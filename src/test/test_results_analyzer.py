import unittest
from results_analyzer import ResultsAnalyzer

class TestResultsAnalyzerMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('\n\nANALYZER TESTS')

    def test_simple_analysis(self):
        print('\nTests small run')
        analyzer = ResultsAnalyzer("past_runs/test_run.csv")
        analyzer.analyze()
        self.assertEqual(analyzer.metadata["num_pieces"], 9)
        self.assertEqual(analyzer.stats["num_runs"], 3)
        self.assertEqual(analyzer.stats["mean_actions"], 19)
        self.assertEqual(analyzer.stats["mean_actions_per_block"], 19)
        self.assertEqual(analyzer.stats["mean_look_at_puzzle_actions"],
                         19)
        self.assertEqual(analyzer.stats["std_dev_actions"], 19)
        self.assertEqual(analyzer.stats["std_dev_look_at_puzzle_actions"],
                         19)
        
