import csv

class ResultsAnalyzer:

    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.results = []
        self._parse_csv()

    def _parse_csv(self):
        with open(self.csv_path, newline='') as csvfile:
            results_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in results_reader:
                self.results.append(row)

    def analyze(self):
        print(self.results)
