from Vertice import Vertice
from Edge import Edge

class Graph:
    # Receive nothing
    def __init__(self):
        self.list_vertices = []
        self.list_edges = []

    # Receive an integer
    def add_vertice(self, identifier):
        self.list_vertices.append(Vertice(identifier))

        
    # Receive an integer
    def find_vertice(self, Id):
        for vert in self.list_vertices:
            if Id == vert.getId():
                return vert
        else:
            return None
        
    # Receive two integers
    def add_edge(self, origin, destination, cost):
        vert_origin = self.find_vertice(origin)
        vert_destination = self.find_vertice(destination)
        
        if (vert_origin is not None) and (vert_destination is not None):
            self.list_edges.append(Edge(vert_origin, vert_destination, cost))
        else:
            print("add_edge: one or both vertices are not valid")

    # Receive two integers
    def find_edge(self, origin, destination):
        vert_origin = self.find_vertice(origin)
        vert_destination = self.find_vertice(destination)
    
        for edg in self.list_edges:
            _origin = edg.getOrigin()
            _destination = edg.getDestination()

            if vert_origin.getId() == _origin.getId() and vert_destination.getId() == _destination.getId():
                return edg

    # Return an integer
    def is_empty(self):
        return len(self.list_edges) == 0
     

    # Receive an vertice
    def adjacent_Search(self, u): 
        for i in range(len(self.list_edges)):
            origin = self.list_edges[i].getOrigin()
            destination = self.list_edges[i].getDestination()
            if (u.getId() == origin.getId()) and (destination.getVisited() == False):
                destination.setVisited(True)
                return destination
        else:
            return None
     
    ### DFS ###    
    def Depth_first_search(self):
        for v in self.list_vertices:
            v.setVisited(False)

        for v in self.list_vertices:
            if not v.getVisited():
                self.visit(v)

    def visit(self, vert):
        print("Visiting vertice: %s" % vert.getId())
        
        vert.setVisited(True)
        
        v = self.adjacent_Search(vert)  # return only not visited or null        
        while v is not None:
            self.visit(v)
            v = self.adjacent_Search(vert)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
