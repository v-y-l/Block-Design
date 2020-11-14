from random import sample
from utils.enums import SearchType
from utils.helper import isTrianglePattern

# Face search functions, given some block, search for a face. '''

'''
  Randomly search for the block pattern.
  Applies the actions to the block,
  then returns those actions as a list.
'''
def random_search(block, dest_pattern, actions):
    if block.getPattern() == dest_pattern:
        return actions
    valid_actions = block.getValidActions()
    next_action = sample(valid_actions, 1)[0]
    actions.append(next_action)
    block.executeAction(next_action)
    return random_search(block, dest_pattern, actions)

'''
   Take the shortest path to find the destination pattern.
'''
def beeline_search(block, dest_pattern, actions):
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
        valid_actions = block.getGoToActions()
        next_action = sample(valid_actions, 1)[0]
        actions.append(next_action)
        block.executeAction(next_action)
        return beeline_search(block, dest_pattern, actions)

'''
   Never go to the same face with this search.
'''
def memory_search(block, dest_pattern, actions):
    pass

# Puzzle piece search functions, given some puzzle,
# return the next puzzle piece to solve for.

def sequential_search(problem):
    return range(len(problem))

face_search_options = {
    'r': random_search,
    'b': beeline_search,
    'm': memory_search
}

puzzle_piece_search_options = {
    's': sequential_search
}
