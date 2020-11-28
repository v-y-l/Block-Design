from block import BlockPattern, Block
from utils.enums import BlockAction
from search import SearchType, random_search, sequential_search

class PuzzleSolver:

    def __init__(self, problem, solvers):
        self.solvers = solvers
        self.problem = problem
        self.blockBank = [Block(1, i+1) for i in range(len(problem))]
        self.actionCounter = {
            BlockAction.GoToFaceOne: 0,
            BlockAction.GoToFaceTwo: 0,
            BlockAction.GoToFaceThree: 0,
            BlockAction.GoToFaceFour: 0,
            BlockAction.GoToFaceFive: 0,
            BlockAction.GoToFaceSix: 0,
            BlockAction.RotateLeft: 0,
            BlockAction.RotateRight: 0
        }

    '''
    Returns a list of actions executed by each block to solve the problem.
    '''
    def solve(self):
        faceSearcher = self.solvers[SearchType.Face]
        puzzlePieceSearcher = self.solvers[SearchType.PuzzlePiece]

        # The actions taken for each block to get to the destination state
        actionsPerBlock = []

        for i in puzzlePieceSearcher(self.problem):
            block = self.blockBank[i]
            searchFaceActions = faceSearcher(
                block,
                self.problem[i],
                actionsPerBlock)
            self.addBlockToStats(block)
            self.printSolvedPuzzlePiece(i)
        self.printPuzzleStats()

        return actionsPerBlock

    def addBlockToStats(self, block):
        for action, count in block.getActionCounter().items():
            self.actionCounter[action] += count

    def printSolvedPuzzlePiece(self, pieceNumber):
        print("...[Solved puzzle piece {}] {}\n".format(
            pieceNumber + 1,
            str(self.blockBank[pieceNumber])))

    def getActionCounter(self):
        return self.actionCounter

    def printPuzzleStats(self):
        print('========================')
        print('| Puzzle statistics... |')
        print('========================')
        for action, count in self.getActionCounter().items():
            print(action, ": ", count)
