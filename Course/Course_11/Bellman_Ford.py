class BellmanFord:
    def __init__(self, n, edges):
        self.n = n  # Number of vertices
        self.edges = edges  # List of edges as (u, v, weight)

    def run(self, start):
        # Step 1: Initialize distances
        M = [[float('inf')] * self.n for _ in range(self.n)]  # Create a matrix for storing distances
        M[start][0] = 0  # Distance to start node is 0

        # Step 2: Relax edges (V - 1) times
        for i in range(1, self.n):
            for v in range(self.n):
                M[v][i] = M[v][i-1]  # Set current distance to the previous distance
                # Relax every edge (u, v)
                for u, v, weight in self.edges:
                    if M[u][i-1] + weight < M[v][i]:
                        M[v][i] = M[u][i-1] + weight

        # Step 3: Output the final shortest distances
        return M


# Example usage
edges = [
    (0, 1, 6),  # S -> A (6)
    (0, 2, 4),  # S -> C (4)
    (1, 3, 1),  # A -> D (1)
    (2, 3, 3),  # C -> D (3)
    (3, 4, 1)   # D -> E (1)
]

n = 5  # Number of vertices
bellman_ford = BellmanFord(n, edges)
start_node = 0  # Start node S

# Run Bellman-Ford algorithm
distances = bellman_ford.run(start_node)

# Output shortest distances from the source node
print("Shortest paths from source S:")
for i in range(n):
    print(f"Distance to node {i}: {distances[i][n-1]}")
