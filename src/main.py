from search import face_search_options, puzzle_piece_search_options, SearchType
from puzzle import Puzzle
from block import BlockPattern

if __name__=="__main__":
    face_search_input = input("Specify face search: [r]andom_search or [b]eeline_search... ")
    puzzle_piece_search_input = input("Specify puzzle piece search: [s]equential_search... ")

    face_search = face_search_options.get(face_search_input, face_search_options['r'])
    puzzle_piece_search = puzzle_piece_search_options.get(
        puzzle_piece_search_input, puzzle_piece_search_options['s'])
    print("\nPuzzle starting...")
    solvers = {
        SearchType.Face: face_search,
        SearchType.PuzzlePiece: puzzle_piece_search
    }
    puzzle = Puzzle([
        BlockPattern.BlackSquare,
        BlockPattern.BlackBottomLeftCornerSquare,
        BlockPattern.BlackTopRightCornerSquare,
        BlockPattern.BlackSquare
    ], {
        SearchType.Face: face_search,
        SearchType.PuzzlePiece: puzzle_piece_search
    })

    print("\nPuzzle solving...")
    puzzle.solve()
