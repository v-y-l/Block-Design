from search import face_search_options, puzzle_piece_search_options, SearchType
from puzzle_solver import PuzzleSolver
from puzzle_image import PuzzleImage, puzzle_options
from block import BlockPattern

if __name__=="__main__":
    puzzle_input = input("Specify puzzle: " +
                              "puzzle_[a].png, puzzle_[b].png, or puzzle_[c].png... ")
    face_search_input = input("Specify face search: " +
                              "[r]andom_search, [b]eeline_search, or [m]emory_search... ")
    puzzle_piece_search_input = input("Specify puzzle piece search: [s]equential_search... ")

    puzzle = puzzle_options.get(puzzle_input, puzzle_options['a'])
    face_search = face_search_options.get(face_search_input, face_search_options['r'])
    puzzle_piece_search = puzzle_piece_search_options.get(
        puzzle_piece_search_input, puzzle_piece_search_options['s'])

    print("\n======================")
    print("| Puzzle starting... |")
    print("======================")

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
