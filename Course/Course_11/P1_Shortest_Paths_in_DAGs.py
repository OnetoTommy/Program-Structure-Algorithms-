class ShortestPathsDAG:
    def __init__(self, numsV):
        self.numsV = numsV  # Number of vertices
        self.graph = [[] for _ in range(self.numsV)]  # Graph representation as adjacency list

    def add_edge(self, start, end, cost):
        """Add an edge from 'start' to 'end' with a given cost"""
        self.graph[start].append((end, cost))

    def topological_sort(self):
        """Topological Sort (using Kahn's Algorithm)"""
        in_degree = [0] * self.numsV  # Array to store the in-degree of each node
        for u in range(self.numsV):
            for v, _ in self.graph[u]:
                in_degree[v] += 1

        queue = []
        for i in range(self.numsV):
            if in_degree[i] == 0:  # If no incoming edges, it can be processed first
                queue.append(i)

        topo_order = []

        while queue:
            u = queue.pop(0)
            topo_order.append(u)
            for v, _ in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return topo_order  # Return the topological order

    def find_shortest_path(self, start):
        """Find the shortest path using dynamic programming in a DAG"""
        dist = [float('inf')] * self.numsV
        dist[start] = 0

        # Get the topological order of the graph
        topo_order = self.topological_sort()

        # Relax the edges in the topological order
        for u in topo_order:
            for v, weight in self.graph[u]:
                # Relax the edge (u, v), update dist[v] if a shorter path is found
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

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
