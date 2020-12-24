import csv

class ResultsAnalyzer:

    def __init__(self,
                 csv_path="past_runs/puzzle_c_beeline_search_skip_unknown_search_0.1_3_1.0_1000.csv",
                 output_file=None
    ):
        self.csv_path = csv_path
        self.output_file = output_file
        self.csv_writer = None
        self.file = None
        self.raw_results = []
        self.stats = {
            "num_runs": 0,
            "mean_actions": 0.0,
            "mean_actions_per_block": 0.0,
            "mean_look_at_puzzle_actions": 0.0,
        }
        self.metadata = {
            "num_pieces": 0
        }
        self._parse_csv()

    def _parse_csv(self):
        with open(self.csv_path, newline='') as csvfile:
            results_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in results_reader:
                self.raw_results.append(row)

    def analyze(self):
        if self.output_file:
            self.file = open(self.output_file, 'a')
            self.csv_writer = csv.writer(self.file,
                                         # A hack, since our true delimiter is ","
                                         delimiter='&',
                                         quoting=csv.QUOTE_NONE)

        if not self.file: self.print("")

        for row in self.raw_results:
            index = int(row[0])
            if index == 0:
                self.stats["num_runs"] += 1
                if self.stats["num_runs"] == 1:
                    for i in range(1, len(row), 2):
                        key, value = row[i], row[i+1]
                        self.metadata[key] = value
                continue

            self.stats["mean_actions"] += 1

            if row[1] == "Puzzle" and row[4] == "LookAtPuzzle":
                self.stats["mean_look_at_puzzle_actions"] += 1
                continue

            if row[1] == "Block":
                self.metadata["num_pieces"] = max(int(row[2]),
                                                  self.metadata["num_pieces"])
                self.stats["mean_actions_per_block"] += 1

        self.stats["mean_actions"] /= self.stats["num_runs"]
        self.stats["mean_look_at_puzzle_actions"] /= self.stats["num_runs"]
        self.stats["mean_actions_per_block"] /= self.metadata["num_pieces"]
        self.stats["mean_actions_per_block"] /= self.stats["num_runs"]

        self.print("PUZZLE CONFIGURATION")
        for key, value in self.metadata.items():
            self.print("{}: {}".format(key, value))

        self.print("\nSOLUTION STATISTICS")
        for key, value in self.stats.items():
            self.print("{}: {}".format(key, value))

        self.print("")

        self.file: self.file.close()

    def print(self, row):
        if self.csv_writer:
            self.csv_writer.writerow([row])
        else:
            print(row)
