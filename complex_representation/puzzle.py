from block import BlockPattern, Block
from search import random_search, SearchType

class Puzzle:

    def __init__(self, problem, solvers):
        self.solvers = solvers
        self.problem = problem
        self.blockBank = [Block(1, i+1) for i in range(len(problem))]

    '''
    Returns a list of actions executed by each block to solve the problem.
    '''
    def solve(self):
        searchFace = self.solvers[SearchType.Face]
        actionsPerBlock = []
        for i in range(len(self.problem)):
            searchFaceActions = searchFace(self.blockBank[i], self.problem[i])
            actionsPerBlock.append(actionsPerBlock)
        return actionsPerBlock
