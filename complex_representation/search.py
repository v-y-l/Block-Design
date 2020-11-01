from random import sample

'''
Randomly search for the block pattern, applying the actions to the block,
then returning those actions as a list.
'''
def random_search(block, dest_pattern):
    actions = []
    if block.getPattern() == dest_pattern:
        return actions
    possible_actions = block.getValidActions()
    next_action = sample(possible_actions, 1)[0]
    actions.append(next_action)
    block.executeAction(next_action)
    return random_search(block, dest_pattern)
