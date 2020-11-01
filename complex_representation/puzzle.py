from block import BlockPattern, Block
from random import sample

class Puzzle:

    def __init__(self, problem, solver_function):
        self.solver_function = solver_function
        self.problem = problem
        self.blockBank = [Block() for i in range(len(problem))]

    '''
    Returns a list of actions by block,
    taken to take solve the problem.
    '''
    def solve(self):
        movesPerBlock = []
        for i in range(len(self.problem)):
            movesPerBlock.append(
                self.solver_function(self.blockBank[i], self.problem[i]))
        return movesPerBlock

def random_search(block, dest_pattern):
    actions = []
    if block.getPattern() == dest_pattern:
        return actions
    possible_actions = block.getValidActions()
    next_action = sample(possible_actions, 1)[0]
    actions.append(next_action)
    block.executeAction(next_action)
    return random_search(block, dest_pattern)
