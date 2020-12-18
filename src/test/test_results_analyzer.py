import unittest
from results_analyzer import ResultsAnalyzer

class TestResultsAnalyzerMethods(unittest.TestCase):

    def test_simple_analysis(self):
        print('\nTests small run')
        analyzer = ResultsAnalyzer("past_runs/test_run.csv")
        analyzer.analyze()
        self.assertEqual(analyzer.stats["num_runs"], 3)
        self.assertEqual(analyzer.stats["mean_actions"], 19)
