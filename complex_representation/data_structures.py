''' For a doubly linked list '''
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


''' A node to represent a face. '''
class BlockNode:
    
    def __init__(self, number):
        self.val = number
        self.neighbors = {}
