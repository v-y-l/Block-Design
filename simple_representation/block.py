from enum import Enum

class Pattern(Enum):
    White = 1
    Black = 2
    Triangle = 3

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

        self.pattern_map = {
            1: Pattern.Triangle,
            2: Pattern.White,
            3: Pattern.White,
            4: Pattern.Black,
            5: Pattern.Black,
            6: Pattern.Triangle
        }

    def getNeighbors(self):
        return self.adjacency_list[self.current_face]

    def getPattern(self):
        return self.pattern_map[self.current_face]

    def getFace(self):
        return self.current_face

    def goToFace(self, next_face):
        if next_face in self.getNeighbors():
            self.current_face = next_face
        else:
            raise Exception("Can't go from {} to {}".format(self.current_face, next_face))
