import csv

class ResultsAnalyzer:

    def __init__(self,
                 csv_path="past_runs/puzzle_c_beeline_search_skip_unknown_search_0.1_3_1.0_1000.csv"):
        self.csv_path = csv_path
        self.raw_results = []
        self.stats = {
            "num_runs": 0,
            "mean_actions": 0.0
        }
        self._parse_csv()

    def _parse_csv(self):
        with open(self.csv_path, newline='') as csvfile:
            results_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in results_reader:
                self.raw_results.append(row)

    def analyze(self):
        for row in self.raw_results:
            index = int(row[0])
            if index == 0:
                self.stats["num_runs"] += 1
            else:
                self.stats["mean_actions"] += 1
        self.stats["mean_actions"] /= self.stats["num_runs"]

    def printStats(self):
        print(self.stats)
