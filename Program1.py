from Graph import Graph

g = Graph()

g.add_vertice(1)
g.add_vertice(2)
g.add_vertice(3)
g.add_vertice(4)
g.add_vertice(5)
g.add_vertice(6)
g.add_vertice(7)
g.add_vertice(8)
g.add_vertice(9)
g.add_vertice(10)

g.add_edge(1,2,2)
g.add_edge(1,3,1)
g.add_edge(2,4,3)
g.add_edge(2,5,3)
g.add_edge(3,6,3)
g.add_edge(3,7,3)
g.add_edge(4,8,3)
g.add_edge(4,9,3)
g.add_edge(4,10,3)

g.Depth_first_search()
print("sucesso")
