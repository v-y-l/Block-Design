from block import BlockPattern, Block
from search import SearchType, random_search, sequential_search

class PuzzleSolver:

    def __init__(self, problem, solvers):
        self.solvers = solvers
        self.problem = problem
        self.blockBank = [Block(1, i+1) for i in range(len(problem))]

    '''
    Returns a list of actions executed by each block to solve the problem.
    '''
    def solve(self):
        faceSearcher = self.solvers[SearchType.Face]
        puzzlePieceSearcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actionsPerBlock = []

        for i in puzzlePieceSearcher(self.problem):
            searchFaceActions = faceSearcher(
                self.blockBank[i],
                self.problem[i],
            actionsPerBlock)
            self.printSolvedPuzzlePiece(i)
        return actionsPerBlock

    def printSolvedPuzzlePiece(self, pieceNumber):
        print("...[Solved puzzle piece {}] {}\n".format(
            pieceNumber + 1,
            str(self.blockBank[pieceNumber])))
