from block import BlockPattern, Block
from search import random_search

class Puzzle:

    '''
    problem is the puzzle image that we want to do block design on,
    solver function locates the correct face of each block for each
    item in the puzzle
    '''
    def __init__(self, problem, solver_function):
        self.solver_function = solver_function
        self.problem = problem
        self.blockBank = [Block(1, i+1) for i in range(len(problem))]

    '''
    Returns a list of actions executed by each block to solve the problem.
    '''
    def solve(self):
        movesPerBlock = []
        for i in range(len(self.problem)):
            movesPerBlock.append(
                self.solver_function(self.blockBank[i], self.problem[i]))
        return movesPerBlock
