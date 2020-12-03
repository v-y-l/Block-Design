from random import sample
from utils.enums import BlockPattern, SearchType
from utils.helper import isTrianglePattern

# Face search functions, given some block, search for a face. '''

'''
  Randomly search for the block pattern.
  Applies the actions to the block,
  then returns those actions as a list.
'''
def random_search(block, dest_pattern, actions):
    if dest_pattern == BlockPattern.Unknown:
        return []
    if block.getPattern() == dest_pattern:
        return actions
    valid_actions = block.getValidActions()
    next_action = sample(valid_actions, 1)[0]
    actions.append(next_action)
    block.executeAction(next_action)
    return random_search(block, dest_pattern, actions)

def beeline_search(block, dest_pattern, actions):
    if dest_pattern == BlockPattern.Unknown:
        return []
    ''' Take the shortest path to find the destination pattern. '''
    if block.getPattern() == dest_pattern:
        return actions
    elif (block.hasTrianglePattern() and isTrianglePattern(dest_pattern)):
        valid_actions = block.getRotateActions()
        # Since the destination face is only two rotations away,
        # taking any default move ensures the ideal move in the next move.
        next_action = valid_actions[0]
        if block.peekAction(valid_actions[0]) == dest_pattern:
            next_action = valid_actions[0]
        elif block.peekAction(valid_actions[1]) == dest_pattern:
            next_action = valid_actions[1]
        actions.append(next_action)
        block.executeAction(next_action)
        return beeline_search(block, dest_pattern, actions)
    else:
        # Once again, since any face is only ever two moves away from
        # any other face, the destination face is only ever two moves away.
        # Taking any default move ensures the ideal move in the next move.
        valid_actions = block.getGoToActions()
        next_action = sample(valid_actions, 1)[0]
        for action in valid_actions:
            if block.peekAction(action) == dest_pattern or isTrianglePattern(dest_pattern) and isTrianglePattern(block.peekAction(action)):
                next_action = action
                break
        actions.append(next_action)
        block.executeAction(next_action)
        return beeline_search(block, dest_pattern, actions)

''' Never go to the same face with this search. '''
def memory_search(block, dest_pattern, actions):
    pass

# Puzzle piece search functions, given some puzzle,
# return the next puzzle piece to solve for.

''' Search the puzzle in sequential order. '''
def sequential_search(problem):
    return range(len(problem))

''' Search the puzzle in sequential order, but skip unknown (forgotten) blocks. '''
def skip_unknown_search(problem):
    pass

face_search_options = {
    'r': random_search,
    'b': beeline_search,
}

puzzle_piece_search_options = {
    's': sequential_search
}
