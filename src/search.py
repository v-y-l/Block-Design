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
    ''' Take the shortest path to find the destination pattern. '''
    if block.get_pattern() == dest_pattern:
        return actions
    elif (block.has_triangle_pattern() and is_triangle_pattern(dest_pattern)):
        valid_actions = block.get_rotate_actions()
        # Since the destination face is only two rotations away,
        # taking any default move ensures the ideal move in the next move.
        next_action = valid_actions[0]
        if block.peek_action(valid_actions[0])[1] == dest_pattern:
            next_action = valid_actions[0]
        elif block.peek_action(valid_actions[1])[1] == dest_pattern:
            next_action = valid_actions[1]
        actions.append(next_action)
        block.execute_action(next_action)
        return beeline_search(block, dest_pattern, actions)
    else:
        # Once again, since any face is only ever two moves away from
        # any other face, the destination face is only ever two moves away.
        # Taking any default move ensures the ideal move in the next move.
        valid_actions = block.get_go_to_actions()
        next_action = sample(valid_actions, 1)[0]
        for action in valid_actions:
            if (
                    block.peek_action(action)[1] == dest_pattern
                    or is_triangle_pattern(dest_pattern)
                    and is_triangle_pattern(block.peek_action(action)[1])
            ):
                next_action = action
                break
        actions.append(next_action)
        block.execute_action(next_action)
        return beeline_search(block, dest_pattern, actions)

''' Never go to the same face with this search. '''
def memory_search(block, dest_pattern, actions):
    # Do random search
    if dest_pattern == BlockPattern.Unknown:
        return []
    if block.get_pattern() == dest_pattern:
        return actions

    if (block.has_triangle_pattern() and is_triangle_pattern(dest_pattern)):
        valid_actions = block.get_rotate_actions()
    else:
        valid_actions = block.get_go_to_actions()
    next_action = valid_actions.pop()
    next_face, next_pattern = block.peek_action(next_action)
    while (next_face, next_pattern) in block.visited:
        next_action = valid_actions.pop()
        next_face, next_pattern = block.peek_action(next_action)
    actions.append(next_action)
    block.execute_action(next_action)
    block.visited.add((block.get_face(), block.get_pattern()))
    return memory_search(block, dest_pattern, actions)

# Puzzle piece search functions, given some puzzle,
# return the next puzzle piece to solve for.

''' Search the puzzle in sequential order. '''
def sequential_search(problem):
    r, c = problem.unsolved_pieces[0]
    unsolved_piece_pattern = problem.get_pattern(r, c)
    if unsolved_piece_pattern == BlockPattern.Unknown:
        problem.look_at_puzzle((r,c), problem.glance_factor)
        unsolved_piece_pattern = problem.get_pattern(r, c)
    return unsolved_piece_pattern, (r, c)

''' Search the puzzle in sequential order, but skip unknown (forgotten) blocks. '''
def skip_unknown_search(problem):
    for r, c in problem.unsolved_pieces:
        unsolved_piece_pattern = problem.get_pattern(r, c)
        if unsolved_piece_pattern != BlockPattern.Unknown:
           return unsolved_piece_pattern, (r, c)
    r, c = problem.unsolved_pieces[0]
    problem.look_at_puzzle((r,c), problem.glance_factor)
    unsolved_piece_pattern = problem.get_pattern(r, c)
    return unsolved_piece_pattern, (r, c)

face_search_options = {
    'memory_search': memory_search,
    'random_search': random_search,
    'beeline_search': beeline_search,
}

puzzle_piece_search_options = {
    'sequential_search': sequential_search,
    'skip_unknown_search': skip_unknown_search,
}
