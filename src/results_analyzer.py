import csv

class ResultsAnalyzer:

    def __init__(self,
                 csv_path="past_runs/puzzle_c_beeline_search_skip_unknown_search_0.1_3_1.0_1000.csv",
                 output_file=None,
                 test_only=False
    ):
        self.csv_path = csv_path
        self.output_file = output_file
        self.test_only = test_only
        self.csv_writer = None
        self.file = None
        self.raw_results = []
        self.stats = {
            "num_runs": 0,
            "min_actions": 0.0,
            "mean_actions": 0.0,
            "max_actions": 0.0,
            "mean_actions_per_block": 0.0,
            "min_look_at_puzzle_actions": 0.0,
            "mean_look_at_puzzle_actions": 0.0,
            "max_look_at_puzzle_actions": 0.0,
            "std_dev_actions": 0.0,
            "std_dev_look_at_puzzle_actions": 0.0,
        }
        self.metadata = {
            "num_pieces": 0,
        }
        self.hidden_metadata = {
            "actions_by_run": [],
            "look_at_puzzle_actions_by_run": [],
        }
        self._parse_csv()

    def _parse_csv(self):
        with open(self.csv_path, newline='') as csvfile:
            results_reader = csv.reader(csvfile,
                                        delimiter=',',
                                        quotechar='|')
            for row in results_reader:
                self.raw_results.append(row)

    def analyze(self):
        if self.output_file:
            self.file = open(self.output_file, 'a')
            self.csv_writer = csv.writer(self.file,
                                         # A hack, since our
                                         # true delimiter is ","
                                         delimiter='&',
                                         quoting=csv.QUOTE_NONE)

        if not self.file: self.print("")

        run_index = 0
        for row in self.raw_results:
            index = int(row[0])
            if index == 0:
                self.stats["num_runs"] += 1
                if self.stats["num_runs"] == 1:
                    for i in range(1, len(row), 2):
                        key, value = row[i], row[i+1]
                        self.metadata[key] = value
                self.hidden_metadata["actions_by_run"].append(0)
                self.hidden_metadata["look_at_puzzle_actions_by_run"].append(0)
                continue

            self.hidden_metadata["actions_by_run"][-1] += 1
            self.stats["mean_actions"] += 1

            if row[1] == "Puzzle" and row[4] == "LookAtPuzzle":
                self.stats["mean_look_at_puzzle_actions"] += 1
                self.hidden_metadata["look_at_puzzle_actions_by_run"][-1] += 1
                continue

            if row[1] == "Block":
                self.metadata["num_pieces"] = max(
                    int(row[2]),
                    self.metadata["num_pieces"])
                self.stats["mean_actions_per_block"] += 1

        self.stats["mean_actions"] /= self.stats["num_runs"]
        self.stats["mean_actions"] = round(self.stats["mean_actions"], 2)

        self.stats["mean_look_at_puzzle_actions"] /= self.stats["num_runs"]
        self.stats["mean_look_at_puzzle_actions"] = round(
            self.stats["mean_look_at_puzzle_actions"], 2)

        self.stats["mean_actions_per_block"] /= self.metadata["num_pieces"]
        self.stats["mean_actions_per_block"] /= self.stats["num_runs"]
        self.stats["mean_actions_per_block"] = round(
            self.stats["mean_actions_per_block"], 2)
        self.stats["min_actions"] = min(
            self.hidden_metadata["actions_by_run"])
        self.stats["max_actions"] = max(
            self.hidden_metadata["actions_by_run"])
        self.stats["min_look_at_puzzle_actions"] = min(
            self.hidden_metadata["look_at_puzzle_actions_by_run"])
        self.stats["max_look_at_puzzle_actions"] = max(
            self.hidden_metadata["look_at_puzzle_actions_by_run"])


        self.set_std_dev("actions_by_run",
                         "std_dev_actions",
                         "mean_actions")
        self.set_std_dev("look_at_puzzle_actions_by_run",
                         "std_dev_look_at_puzzle_actions",
                         "mean_look_at_puzzle_actions")

        if not self.test_only:
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

    def set_std_dev(self, hidden_key, stats_std_dev_key, stats_mean_key):
        for num_actions in self.hidden_metadata[hidden_key]:
            self.stats[stats_std_dev_key] += (
                num_actions - self.stats[stats_mean_key]) ** 2
        self.stats[stats_std_dev_key] /= self.stats["num_runs"]
        self.stats[stats_std_dev_key] **= .5
