from random import sample
from utils.enums import SearchType

# Face search functions, given some block, search for a face. '''

'''
  Randomly search for the block pattern.
  Applies the actions to the block,
  then returns those actions as a list.
'''
def random_search(block, dest_pattern, actions):
    if block.getPattern() == dest_pattern:
        return actions
    possible_actions = block.getValidActions()
    next_action = sample(possible_actions, 1)[0]
    actions.append(next_action)
    block.executeAction(next_action)
    return random_search(block, dest_pattern, actions)

'''
   Take the shortest path to find the destination pattern.
'''
def beeline_search(block, dest_pattern, actions):
    #if (block.hasTrianglePattern() and isTrianglePattern(pattern)):
    pass

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
