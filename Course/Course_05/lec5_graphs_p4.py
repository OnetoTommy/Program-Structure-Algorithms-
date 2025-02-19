import  networkx as nx
import matplotlib.pyplot as plt

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.neighbors = []
        self.pre = -1
        self.post = -1
        self.prev = -1
        self.visited = False
        self.CC = -1

    def add_neighbor(self, neighbor_id):
        if neighbor_id not in self.neighbors:
            self.neighbors.append(neighbor_id)
class Graph:
    def __init__(self):
        self.vertices = {}
        self.CCnum = 0
        self.clock = 1
        self.isDirected = False
        self.visual = []

    def add_vertex(self, vertex):
        if vertex.id not in self.vertices and isinstance(vertex, Vertex):
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbor(v2)
            self.vertices[v2].add_neighbor(v1)
            self.visual.append([v1, v2])
            return True
        else:
            return False

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add_neighbor(v2)
            self.visual.append([v1, v2])
            self.isDirected = True
            return True
        else:
            return False

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def visualize(self):
        if self.isDirected == True:
            G = nx.DiGraph()
        else:
            G = nx.Graph()

        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()

    def explore(self, v):
        v.visited = True
        self.CC = self.CCnum
        v.pre = self.clock
        self.clock += 1

        for uId in v.neighbors:
            u = self.vertices[uId]
            if u.visited == False:
                self.explore(u)
                self.prev = v.id
        self.post = self.clock
        self.clock += 1

    def DFS(self):
        for vId, v in self.vertices.items():
            if v.visited == False:
                self.explore(v)
                self.CCnum +=1

        ##print pre and post values
        print("***Details***\n")
        for vId, v in self.vertices.items():
            print("Vertex= %d pre= %d post = %d ; CC = %d prev = %d" % (vId, v.pre, v.post, v.CC, v.prev))


# Create a graph with 4 vertices and 5 edges
graph = Graph()
for i in range(4):
    graph.add_vertex(Vertex(i))

# 1: undir; 2: dir
ex = 3

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

graph.DFS()
graph.visualize()


