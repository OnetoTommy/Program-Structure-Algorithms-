def floyd_warshall(n, graph):
    # Initialize the distance matrix
    dist = [[float('inf')] * n for _ in range(n)]

    # Distance to self is 0
    for i in range(n):
        dist[i][i] = 0

    # Initialize with edge weights from the graph
    for u in range(n):
        for v, weight in graph[u]:
            dist[u][v] = weight

    # Floyd-Warshall algorithm (bottom-up dynamic programming)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Example usage
# Define the graph as an adjacency list
# Each list entry contains tuples (neighbor, edge weight)
graph = [
    [(1, 6), (2, 4)],  # Edges from vertex 0
    [(3, 1)],  # Edges from vertex 1
    [(3, 3)],  # Edges from vertex 2
    [(4, 1)],  # Edges from vertex 3
    []  # Vertex 4 has no outgoing edges
]

n = 5  # Number of vertices
shortest_paths = floyd_warshall(n, graph)

# Print the shortest path distance matrix
print("Shortest paths between all pairs of vertices:")
for row in shortest_paths:
    print(row)
