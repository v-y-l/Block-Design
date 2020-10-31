class EdgeNode:

    def __init__(self, val):

        self.val = val
        self.next = None
    

class Block:

    def __init__(self):

        self.vertices = {
            A: (0,1,1),
            B: (1,1,1),
            C: (0,0,1),
            D: (1,0,1),
            E: (0,1,0),
            F: (1,1,0),
            G: (0,0,0),
            H: (1,0,0)
        }

        AB = EdgeNode(('A', 'B'))
        CD = EdgeNode(('C', 'D'))
        EF = EdgeNode(('E', 'F'))
        GH = EdgeNode(('G', 'H'))

        AB.next = EF
        EF.next = GH
        GH.next = CD
        CD.next = AB

    def _findAxis(self):
        pass
        
    def flipUp(self):
        pass
        
