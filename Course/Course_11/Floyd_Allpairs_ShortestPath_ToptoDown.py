def FW_Recur(V, i, j, k, w, memo):
    # If we've already computed the shortest path from i to j using the first k vertices, return it
    if memo[i][j][k] != -1:
        return memo[i][j][k]

    # Base case: when no intermediate vertices are left
    if k == 0:
        return w[i][j]

    # Recur: Check if there's a shorter path via the k-th vertex
    memo[i][j][k] = min(
        FW_Recur(V, i, j, k - 1, w, memo),  # Exclude k
        FW_Recur(V, i, k, k - 1, w, memo) + FW_Recur(V, k, j, k - 1, w, memo)  # Include k
    )

    return memo[i][j][k]


def floyd_warshall(V, w):
    # Initialize memoization table with -1 (indicating no value computed yet)
    memo = [[[-1 for _ in range(len(V))] for _ in range(len(V))] for _ in range(len(V))]

    # Apply Floyd-Warshall using recursion and memoization
    dist = [[0 for _ in range(len(V))] for _ in range(len(V))]

    for i in range(len(V)):
        for j in range(len(V)):
            dist[i][j] = FW_Recur(V, i, j, len(V) - 1, w, memo)

    return dist


# Example graph with 4 vertices (0, 1, 2, 3)
# Adjacency matrix representing edge weights between vertices
w = [
    [0, 6, 4, float('inf')],  # Edges from 0
    [float('inf'), 0, float('inf'), 1],  # Edges from 1
    [float('inf'), float('inf'), 0, 3],  # Edges from 2
    [float('inf'), float('inf'), float('inf'), 0]  # Edges from 3
]

V = [0, 1, 2, 3]  # Vertices in the graph

# Run Floyd-Warshall
shortest_paths = floyd_warshall(V, w)

# Output the shortest path matrix
print("Shortest paths between all pairs of vertices:")
for row in shortest_paths:
    print(row)
