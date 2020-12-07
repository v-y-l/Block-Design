from search import face_search_options, puzzle_piece_search_options, SearchType
from puzzle_image_solver import PuzzleImageSolver, puzzle_options
from block_image import BlockPattern
from getopt import getopt, GetoptError
from sys import argv, exit

import csv

if __name__=="__main__":
    puzzle_input = ''
    face_search_input = ''
    puzzle_piece_search_input = ''
    csv_input = ''
    puzzle_memory_loss_factor = 1.0
    try:
        opts, args = getopt(argv[1:], "",
            ["puzzle=", "face_search=", "piece_search=", "puzzle_memory_loss=", "csv="])
        for opt, arg in opts:
            if opt == '-h':
                print('main.py --puzzle <puzzle_[a].png, puzzle_[b].png, or puzzle_[c].png> ' +
                      '--face_search <[r]andom_search or [b]eeline_search> ' +
                      '--piece_search <[s]equential_search> ' +
                      '-puzzle_memory_loss <.5> --csv <example.csv>')
                exit()
            elif opt in ("--puzzle"):
                puzzle_input = arg
            elif opt in ("-f", "--face_search"):
                face_search_input = arg
            elif opt in ("-s", "--piece_search"):
                puzzle_piece_search_input = arg
            elif opt in ("-l", "--puzzle_memory_loss"):
                puzzle_memory_loss_factor = float(arg)
            elif opt in ("-c", "--csv"):
                csv_input = arg
    except GetoptError as err:
        print(err)
        exit(2)

    if puzzle_input == '':
        puzzle_input = input("Specify puzzle: " +
                             "puzzle_[a].png, puzzle_[b].png, or puzzle_[c].png... ")

    if face_search_input == '':
        face_search_input = input("Specify face search: " +
                                  "[r]andom_search or [b]eeline_search... ")

    if puzzle_piece_search_input == '':
        puzzle_piece_search_input = input("Specify puzzle piece search: [s]equential_search... ")       

    puzzle_image = puzzle_options.get(puzzle_input, puzzle_options['a'])
    face_search = face_search_options.get(face_search_input, face_search_options['r'])
    puzzle_piece_search = puzzle_piece_search_options.get(
        puzzle_piece_search_input, puzzle_piece_search_options['s'])
    
    config = {
        'puzzle_memory_loss_factor': puzzle_memory_loss_factor
    }

    print("\n======================")
    print("| Puzzle starting... |")
    print("======================")

    print("[Configuration] Puzzle '{}', face search '{}', puzzle piece search '{}'".format(
        puzzle_input, face_search_input, puzzle_piece_search_input))

    solvers = {
        SearchType.Face: face_search,
        SearchType.PuzzlePiece: puzzle_piece_search
    }
    puzzle_solver = PuzzleImageSolver(puzzle_image, {
        SearchType.Face: face_search,
        SearchType.PuzzlePiece: puzzle_piece_search
    }, config)

    print("\n=====================")
    print("| Puzzle solving... |")
    print("=====================")
    puzzle_solver.solve()

    print("\n==================")
    print("| Puzzle solved! |")
    print("==================")

    if csv_input != '':
        with open(csv_input, 'a', newline='') as csvfile:
            record_writer = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            record_writer.writerow([puzzle_input, face_search_input, puzzle_piece_search_input])
            for action, count in puzzle_solver.get_action_counter().items():
                record_writer.writerow([action, count])
            print("...aggregate stats written to {}".format(csv_input))
