from operator import truediv

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.visited = set()
        self.pre = {}
        self.post = {}
        self.prev = -1
        self.CC = -1
        self.clock = 1
        self.CCnum = 0


    def explore(self,graph, v):
        self.visited.add(v)
        self.pre[v] = self.clock
        self.clock += 1
        self.CC = self.CCnum

        for w in graph[v]:
            if w not in self.visited:
                self.explore(graph, w)


        self.post[v] = self.clock
        self.clock += 1



    def dfs(self,graph):
        for v in graph:
            if v not in self.visited:
                self.CCnum += 1
                self.explore(graph,v)




# Example Graph (Adjacency List)
graph = {
    'A': ['C'],
    'B': ['C'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}


G = Graph()
G.dfs(graph)
print("Pre-order:", G.pre)
print("Post-order:", G.post)