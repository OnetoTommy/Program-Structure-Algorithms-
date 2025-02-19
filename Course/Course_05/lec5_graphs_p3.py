import networkx as nx
from matplotlib import pyplot as plt


class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = []
        self.pre = -1
        self.post = -1
        self.prev = -1
        self.visited = False
        self.CC = -1
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.visual = []
        self.isdirected = False
        self.CCnum = 0
        self.clock = 1

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbor(self.vertices[v2])
            self.vertices[v2].add_neighbor(self.vertices[v1])
            self.visual.append([v1,v2])
            return True
        else:
            return False

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbor(self.vertices[v2])
            self.visual.append([v1,v2])
            self.isdirected = True
            return True
        else:
            return False

    def get_vertex(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def explore(self, v):
        v.visited = True
        v.pre = self.clock
        self.clock += 1
        v.CC = self.CCnum

        for uId in v.neighbors:
            if uId in self.vertices:
                u = self.vertices[uId]
                if u.visited == False:
                    self.explore(u)
                    u.prev = v.id

        v.post = self.clock
        self.clock += 1


    def DFS(self):
        for vId, v in self.vertices.items():
            if v.visited == False:
                self.CCnum += 1
                self.explore(v)

    def visualize(self):
        if self.isdirected == False:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

# Create a graph with 4 vertices and 5 edges
graph = Graph()
for i in range(6):
    graph.add_vertex(Vertex(i))

# 1: undir; 2: dir
ex= 1

if ex == 1:
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(4, 2)
    graph.add_edge(5, None)

elif ex == 2:
    graph.add_directed_edge(0, 1)
    graph.add_directed_edge(0, 2)
    graph.add_directed_edge(1, 2)
    graph.add_directed_edge(1, 3)
    graph.add_directed_edge(2, 3)
elif ex == 3:
    graph.add_directed_edge(0, 1)
    graph.add_directed_edge(0, 2)
    graph.add_directed_edge(3, 0)
    graph.add_directed_edge(3, 2)

graph.DFS()
graph.visualize()