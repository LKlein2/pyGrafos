from Graph import Graph

g = Graph()

g.add_vertice_heuristic("S", 8)
g.add_vertice_heuristic("B", 7)
g.add_vertice_heuristic("C", 3)
g.add_vertice_heuristic("D", 1)
g.add_vertice_heuristic("E", 7)
g.add_vertice_heuristic("F", 6)
g.add_vertice_heuristic("G", 0)
g.add_vertice_heuristic("H", 100)

g.add_edge("S", "C", 1)
g.add_edge("S", "B", 1)
g.add_edge("C", "H", 1)
g.add_edge("B", "C", 1)
g.add_edge("B", "D", 9)
g.add_edge("H", "G", 1)
g.add_edge("D", "G", 1)
g.add_edge("B", "E", 1)
g.add_edge("E", "F", 1)
g.add_edge("D", "F", 1)

g.Greedy_search(g.find_vertice("S"), g.find_vertice("G"))

for i in range (len(g.list_path)):
    print (g.list_path[i].getId())
