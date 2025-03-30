from collections import defaultdict

class Graph:
    def __init__(self, numV):
        self.numV = numV

        #adjacency list
        self.graph = defaultdict(list)

    def add_directed_edge(self, u, v, w):
        self.graph[u].append((v,w))

    def topological_sort(self, v, visited, stack):
        visited[v] = True
        if v in self.graph.keys():
            for u, wt in self.graph[v]:
                if visited[u] == False:
                    self.topological_sort(u, visited, stack)
        stack.append(v)

    def find_shortest_path(self, src):
        visited = [False] * self.numV
        stack = []
        for i in range(self.numV):
            if visited[i] == False:
                self.topological_sort(src, visited, stack)
        
        dist = [float("inf")] * (self.numV)
        dist[src] = 0

        while stack:
            v = stack.pop()
            for u, wt in self.graph[v]:
                if dist[u] > dist[v] + wt:
                    dist[u] = dist[v] + wt

        for i in range(self.numV):
            if dist[i] != float("inf"):
                print("%d : %d"%(i, dist[i]))
            #print(("%d" %dist[i] if dist[i] != float("inf") else "inf", end=" "))


# Example

g = Graph(6)

g.add_directed_edge(0, 1, 1)
g.add_directed_edge(0, 3, 2)
g.add_directed_edge(1, 2, 6)
g.add_directed_edge(2, 4, 1)
g.add_directed_edge(2, 5, 2)
g.add_directed_edge(3, 1, 4)
g.add_directed_edge(3, 4, 3)
g.add_directed_edge(4, 5, 1)

src = 0
g.find_shortest_path(src)