from search import face_search_options, puzzle_piece_search_options, SearchType
from puzzle_image_solver import PuzzleImageSolver
from block_image import BlockPattern
from utils.constants  import PUZZLE_OPTIONS
from getopt import getopt, GetoptError
from sys import argv, exit

if __name__=="__main__":
    puzzle_input = ''
    face_search_input = ''
    puzzle_piece_search_input = ''
    csv_input = ''
    puzzle_memory_loss_factor_input = 0.0
    puzzle_memory_loss_counter_limit_input = 0
    glance_factor_input = 1
    try:
        opts, args = getopt(argv[1:], "h",
            ["puzzle=",
             "face_search=",
             "piece_search=",
             "puzzle_memory_loss=",
             "puzzle_memory_loss_counter_limit=",
             "glance_factor=",
             "csv="])
        for opt, arg in opts:
            if opt == '-h':
                print('main.py --puzzle <[puzzle_a].png, [puzzle_b].png, or [puzzle_c].png> ' +
                      '--face_search <[random_search] or [beeline_search]> ' +
                      '--piece_search <sequential_search> ' +
                      '-puzzle_memory_loss <[0-1]> ' +
                      '-puzzle_memory_loss_counter_limit <[>0]> ' +
                      '-glance_factor <[0-1]> ' +
                      '--csv <example.csv>')
                exit()
            elif opt in ("--puzzle"):
                puzzle_input = arg
            elif opt in ("--face_search"):
                face_search_input = arg
            elif opt in ("--piece_search"):
                puzzle_piece_search_input = arg
            elif opt in ("--puzzle_memory_loss"):
                puzzle_memory_loss_factor_input = float(arg)
            elif opt in ("--puzzle_memory_loss_counter_limit"):
                puzzle_memory_loss_counter_limit_input = int(arg)
            elif opt in ("--glance_factor"):
                glance_factor_input = float(arg)
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

    if not 0 <= glance_factor_input <= 1:
        raise Exception("Specify glance factor: 0-1")

    face_search = face_search_options[face_search_input]
    puzzle_piece_search = puzzle_piece_search_options[puzzle_piece_search_input]

    puzzle_solver_config = {
        'puzzle_memory_loss_factor': puzzle_memory_loss_factor_input,
        'puzzle_memory_loss_counter_limit': puzzle_memory_loss_counter_limit_input,
        'glance_factor': glance_factor_input,
        'solvers': {
            SearchType.Face: face_search,
            SearchType.PuzzlePiece: puzzle_piece_search
        }
    }
    puzzle_solver = PuzzleImageSolver(puzzle_input, puzzle_solver_config)

    puzzle_solver.solve()
    puzzle_solver.print_history(csv_input)
