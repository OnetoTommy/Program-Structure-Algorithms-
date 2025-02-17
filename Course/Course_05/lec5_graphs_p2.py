import networkx as nx
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self,vertex_id):
        self.id = vertex_id
        self.pre = -1
        self.post = -1
        self.prev = -1
        self.CC = -1
        self.visited = False
        self.neighbors = []

    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

class Graph:
    def __init__(self):
        self.vertices = {}
        self.visual = []
        self.CCnum = 0
        self.isDirected = False
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

    def add_directed_edge(self, from_v1, to_v2):
        if from_v1 in self.vertices and to_v2 in self.vertices:
            self.vertices[from_v1].add_neighbor(self.vertices[to_v2])
            self.isDirected = True
            self.visual.append([from_v1,to_v2])
            return True
        else:
            return False


    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def visualize(self):
        if self.isDirected == False:
            g = nx.Graph()
        else:
            g = nx.DiGraph()

        g.add_edges_from(self.visual)
        nx.draw_networkx(g)
        plt.show()

    def explore(self, v):
        v.visited = True
        v.CC = self.CCnum
        v.pre = self.clock
        self.clock += 1

        for uID in v.neighbors:
            if uID in self.vertices:
                u = self.vertices[uID]
                if u.visited == False:
                    self.explore(u)
                    u.prev = v.id

        v.post = self.clock
        self.clock += 1

    def dfs(self):
        for vId, v in self.vertices.items():
            if v.visited == False:
                self.CCnum += 1
                self.explore(v)

        print("***Details***\n")
        for vId, v in self.vertices.items():
            print("Vertex= %d pre= %d post = %d ; CC = %d prev = %d" % (vId, v.pre, v.post, v.CC, v.prev))

# Create a graph with 4 vertices and 5 edges
graph = Graph()
for i in range(4):
    graph.add_vertex(Vertex(i))

# 1: undir; 2: dir
ex= 3

if ex == 1:
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
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

graph.dfs()
graph.visualize()




