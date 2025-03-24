from collections import deque


class ShortestPathsDAG:
    def __init__(self, nums):
        self.nums = nums
        self.graph = [[] for _ in range(self.nums)]
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def topological_sort(self):
        in_degree = [0] * (self.nums)
        for u in range(self.nums):
            for v, w in self.graph[u]:
                in_degree[v] += 1

        queue = []

        for i in in_degree:
            if in_degree[i] == 0:
                queue.append(i)

        topological = []
        while queue:
            v = queue.pop(0)
            topological.append(v)
            for u, w in self.graph[v]:
                in_degree[u] -= 1
                if in_degree[u] == 0:
                    queue.append(u)
        return topological

    def find_shortest_path(self, src):
        dist = [float('inf')] * (self.nums)
        dist[src] = 0
        topo = self.topological_sort()
        for v in topo:
            for u, w in self.graph[v]:
                if dist[v] != float('inf') and dist[v] + w < dist[u]:
                    dist[u] = dist[v] + w

        return dist


# Example usage
graph = ShortestPathsDAG(5)
graph.add_edge(0, 1, 6)  # S -> A (6)
graph.add_edge(0, 2, 4)  # S -> C (4)
graph.add_edge(1, 3, 1)  # A -> D (1)
graph.add_edge(2, 3, 3)  # C -> D (3)
graph.add_edge(3, 4, 1)  # D -> E (1)

# Find shortest path from node 0 (S)
start_node = 0
distances = graph.find_shortest_path(start_node)

# Output shortest distances from the source node
print("Shortest paths from source S:")
for i, d in enumerate(distances):
    print(f"Distance to node {i}: {d}")