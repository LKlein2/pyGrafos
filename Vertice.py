class Vertice:
    # Receive an integer
    def __init__(self, idetifier, heuristic = 0):
        self.idetifier = idetifier
        self.visited = False
        self.heuristic = heuristic
        
    # Return an integer
    def getId(self):
        return self.idetifier
    
    def getVisited(self):
        return self.visited
        
    def setVisited(self, value):
        self.visited = value

    def setHeuristic(self, value):
        self.heuristic = value

    def getHeuristic(self):
        return self.heuristic