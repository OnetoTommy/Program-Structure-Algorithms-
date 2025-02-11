import networkx as nx 
import matplotlib.pyplot as plt 

class Vertex:
    def __init__(self, vertex_id):
        self.id = vertex_id
        self.visited = False
        self.CC = -1
        self.pre = -1
        self.post = -1
        self.prev = -1
        self.dist = float('inf')
        self.neighbors = []


    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)


class Graph:
    def __init__(self):
        self.vertices = {} ## dictionary to store details on every vertex in graph
        self.visual = []
        self.CCNum = 0
        self.clock = 1
        self.isDir = False


    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False


    def add_edge(self, v1, v2, isDirected = False):
        if v1 in self.vertices and v2 in self.vertices:
            if isDirected == False:
                self.vertices[v1].add_neighbor(v2)
                self.vertices[v2].add_neighbor(v1)
            else:
                self.vertices[v1].add_neighbor(v2)
                self.isDir = True
            temp = [v1, v2] 
            self.visual.append(temp) 
            return True
        else:
            return False
        
    def get_vertices(self):
        return self.vertices.keys()


    def __iter__(self):
        return iter(self.vertices.values())
    
    def visualize(self):
        if self.isDir == False:
            G = nx.Graph()
        else:
            G = nx.DiGraph()
        G.add_edges_from(self.visual) 
        nx.draw_networkx(G) 
        plt.show() 

    def explore(self, v):
 
        # Mark the current node as visited
        # and print it
        v.visited = True
        v.CC = self.CCNum
        v.pre = self.clock
        self.clock += 1
        print("Exploring vertex: %d"%(v.id))
 
        # Recur for all the vertices adjacent to this vertex
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
                self.CCNum += 1
                self.explore(v)

        ##print pre and post values
        print("***Details***\n")
        for vId, v in self.vertices.items():
            print("Vertex= %d pre= %d post = %d ; CC = %d prev = %d"%(vId, v.pre, v.post, v.CC, v.prev))
        print("\n")

    def BFS(self, src = -1):
        if src == -1:
            src = min(self.vertices.keys())
        print("Starting BFS with src: %d"%(src))
        queue = []

        queue.append(src)
        self.vertices[src].dist = 0

        while queue:
            uId = queue.pop(0)
            print(uId, end=" ")
            u = self.vertices[uId]

            # Recur for all the vertices adjacent to this vertex
            for vId in u.neighbors:
                if vId in self.vertices:
                    v = self.vertices[vId]
                    if v.dist == float('inf'):
                        v.dist = u.dist + 1
                        queue.append(vId)
                        v.prev = uId

        ## print distances
        print("\n")
        for uId, u in self.vertices.items():
            print("Node: %d ; dist: %f ; prev: %d"%(uId, u.dist, u.prev))

        print("\n")


# Create a graph with 4 vertices and 5 edges
graph = Graph()
for i in range(4):
    graph.add_vertex(Vertex(i))

ex = 1

if ex == 1:
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
elif ex == 2:
    isDir = False
    graph.add_edge(0, 1, isDir)
    graph.add_edge(0, 2, isDir)
    graph.add_edge(1, 2, isDir)
    graph.add_edge(1, 3, isDir)
    graph.add_edge(2, 3, isDir)

#graph.DFS()
#graph.BFS()
#graph.visualize()

graph1 = Graph()
for i in range(4):
    graph1.add_vertex(Vertex(i))

isDir = True
graph1.add_edge(0, 1, isDir)
graph1.add_edge(0, 2, isDir)
graph1.add_edge(1, 2, isDir)
graph1.add_edge(2, 0, isDir)
graph1.add_edge(2, 3, isDir)
graph1.add_edge(3, 3, isDir)

graph1.BFS(2)
graph1.visualize()

graph2 = Graph()
for i in range(6):
    graph2.add_vertex(Vertex(i))
isDir = False
graph2.add_edge(0, 1, isDir)
graph2.add_edge(0, 3, isDir)
graph2.add_edge(0, 5, isDir)
graph2.add_edge(1, 2, isDir)
graph2.add_edge(2, 3, isDir)
graph2.add_edge(3, 4, isDir)
graph2.add_edge(4, 5, isDir)

graph2.BFS()
graph2.visualize()






