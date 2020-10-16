class Block:

    def __init__(self):
        self.current_face = 1
        
        self.adjacency_list = {
            1: {5, 4, 3, 2},
            2: {1, 3, 6, 5},
            3: {1, 4, 6, 2},
            4: {1, 5, 6, 2},
            5: {1, 2, 6, 4},
            6: {3, 4, 5, 2},
        }

    def getNeighbors():
        return self.adjacency_list[self.current_face]
