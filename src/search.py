from random import sample
from utils.enums import BlockPattern, SearchType
from utils.helper import is_triangle_pattern

# Face search functions, given some block, search for a face. '''

'''
  Randomly search for the block pattern.
  Applies the actions to the block,
  then returns those actions as a list.
'''
def random_search(block, dest_pattern, actions):
    if dest_pattern == BlockPattern.Unknown:
        return []
    if block.get_pattern() == dest_pattern:
        return actions
    valid_actions = block.get_valid_actions()
    next_action = sample(valid_actions, 1)[0]
    actions.append(next_action)
    block.execute_action(next_action)
    return random_search(block, dest_pattern, actions)

def beeline_search(block, dest_pattern, actions):
    if dest_pattern == BlockPattern.Unknown:
        return []
    ''' _take the shortest path to find the destination pattern. '''
    if block.get_pattern() == dest_pattern:
        return actions
    elif (block.has_triangle_pattern() and is_triangle_pattern(dest_pattern)):
        valid_actions = block.get_rotate_actions()
        # _since the destination face is only two rotations away,
        # taking any default move ensures the ideal move in the next move.
        next_action = valid_actions[0]
        if block.peek_action(valid_actions[0]) == dest_pattern:
            next_action = valid_actions[0]
        elif block.peek_action(valid_actions[1]) == dest_pattern:
            next_action = valid_actions[1]
        actions.append(next_action)
        block.execute_action(next_action)
        return beeline_search(block, dest_pattern, actions)
    else:
        # _once again, since any face is only ever two moves away from
        # any other face, the destination face is only ever two moves away.
        # _taking any default move ensures the ideal move in the next move.
        valid_actions = block.get_go_to_actions()
        next_action = sample(valid_actions, 1)[0]
        for action in valid_actions:
            if (
                    block.peek_action(action) == dest_pattern
                    or is_triangle_pattern(dest_pattern)
                    and is_triangle_pattern(block.peek_action(action))
            ):
                next_action = action
                break
        actions.append(next_action)
        block.execute_action(next_action)
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
    'random_search': random_search,
    'beeline_search': beeline_search,
}

puzzle_piece_search_options = {
    'sequential_search': sequential_search
}
