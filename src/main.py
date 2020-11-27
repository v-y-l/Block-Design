from search import face_search_options, puzzle_piece_search_options, SearchType
from puzzle_solver import PuzzleSolver
from puzzle_image import PuzzleImage, puzzle_options
from block import BlockPattern
from getopt import getopt, GetoptError
from sys import argv, exit

import csv

if __name__=="__main__":
    puzzle_input = ''
    face_search_input = ''
    puzzle_piece_search_input = ''
    csv_input = ''
    try:
        opts, args = getopt(argv[1:],"hp:f:s:c:",
            ["puzzle=", "facesearch=", "piecesearch=", "csv="])
        for opt, arg in opts:
            if opt == '-h':
                print('main.py -p <puzzle_[a].png, puzzle_[b].png, or puzzle_[c].png> ' +
                      '-f <[r]andom_search or [b]eeline_search> -s <[s]equential_search> ' +
                      '-c <example.csv>')
                exit()
            elif opt in ("-p", "--puzzle"):
                puzzle_input = arg
            elif opt in ("-f", "--facesearch"):
                face_search_input = arg
            elif opt in ("-s", "--piecesearch"):
                puzzle_piece_search_input = arg
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

    puzzle = puzzle_options.get(puzzle_input, puzzle_options['a'])
    face_search = face_search_options.get(face_search_input, face_search_options['r'])
    puzzle_piece_search = puzzle_piece_search_options.get(
        puzzle_piece_search_input, puzzle_piece_search_options['s'])

    print("\n======================")
    print("| Puzzle starting... |")
    print("======================")

    print("[Configuration] Puzzle '{}', face search '{}', puzzle piece search '{}'".format(
        puzzle_input, face_search_input, puzzle_piece_search_input))

    solvers = {
        SearchType.Face: face_search,
        SearchType.PuzzlePiece: puzzle_piece_search
    }
    puzzle_solver = PuzzleSolver(puzzle.getPuzzle(), {
        SearchType.Face: face_search,
        SearchType.PuzzlePiece: puzzle_piece_search
    })

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
            for action, count in puzzle_solver.getActionCounter().items():
                record_writer.writerow([action, count])
