import math

class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, w):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, w))

    def neighbors(self, node):
        return self.adj.get(node, [])

    def heuristic_euclidean(self, a, b, positions):
        x1, y1 = positions[a]
        x2, y2 = positions[b]
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
