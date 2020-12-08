from search import face_search_options, puzzle_piece_search_options, SearchType
from puzzle_image_solver import PuzzleImageSolver
from block_image import BlockPattern
from utils.constants  import PUZZLE_OPTIONS
from getopt import getopt, GetoptError
from sys import argv, exit

import csv

if __name__=="__main__":
    puzzle_input = ''
    face_search_input = ''
    puzzle_piece_search_input = ''
    csv_input = ''
    puzzle_memory_loss_factor_input = 1.0
    try:
        opts, args = getopt(argv[1:], "h",
            ["puzzle=", "face_search=", "piece_search=", "puzzle_memory_loss=", "csv="])
        for opt, arg in opts:
            if opt == '-h':
                print('main.py --puzzle <[puzzle_a].png, [puzzle_b].png, or [puzzle_c].png> ' +
                      '--face_search <random_search or beeline_search> ' +
                      '--piece_search <sequential_search> ' +
                      '-puzzle_memory_loss <0-1> --csv <example.csv>')
                exit()
            elif opt in ("--puzzle"):
                puzzle_input = arg
            elif opt in ("--face_search"):
                face_search_input = arg
            elif opt in ("--piece_search"):
                puzzle_piece_search_input = arg
            elif opt in ("--puzzle_memory_loss"):
                puzzle_memory_loss_factor_input = float(arg)
            elif opt in ("--csv"):
                csv_input = arg
    except GetoptError as err:
        print(err)
        exit(2)

    if puzzle_input not in PUZZLE_OPTIONS:
        raise Exception("Specify puzzle: " +
                        "[puzzle_a].png, [puzzle_b].png, or [puzzle_c].png")

    if face_search_input not in face_search_options:
        raise Exception("Specify face search: " +
                        "random_search or beeline_search")

    if puzzle_piece_search_input not in puzzle_piece_search_options:
        raise Exception("Specify puzzle piece search: [s]equential_search")

    if not 0 <= puzzle_memory_loss_factor_input <= 1:
        raise Exception("Specify puzzle memory loss factor: 0-1")

    face_search = face_search_options[face_search_input]
    puzzle_piece_search = puzzle_piece_search_options[puzzle_piece_search_input]

    puzzle_solver_config = {
        'puzzle_memory_loss_factor': puzzle_memory_loss_factor_input,
        'solvers': {
            SearchType.Face: face_search,
            SearchType.PuzzlePiece: puzzle_piece_search
        }
    }
    puzzle_solver = PuzzleImageSolver(puzzle_input, puzzle_solver_config)

    puzzle_solver.solve()
    puzzle_solver.print_history()

    if csv_input != '':
        with open(csv_input, 'a', newline='') as csvfile:
            record_writer = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            record_writer.writerow([puzzle_input, face_search_input, puzzle_piece_search_input])
            for action, count in puzzle_solver.get_action_counter().items():
                record_writer.writerow([action, count])
            print("...aggregate stats written to {}".format(csv_input))
