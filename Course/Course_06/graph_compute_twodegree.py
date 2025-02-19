def compute_twodegree(adj):
    """
    Computes twodegree[u] = sum of degrees of u's neighbors.

    Parameters:
    adj (dict): Adjacency list representing the graph.
                Keys are vertices, values are lists of neighbors.

    Returns:
    dict: twodegree values for each vertex.
    """
    # Step 1: Compute degree of each vertex
    degree = {u: len(neighbors) for u, neighbors in adj.items()}

    # Step 2: Compute twodegree[u] by summing the degrees of u's neighbors
    twodegree = {}
    for u, neighbors in adj.items():
        twodegree[u] = sum(degree[v] for v in neighbors)

    return twodegree


# Example Graph (Adjacency List)
graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [3, 5],
    5: [3, 4, 6],
    6: [5]
}

# Compute twodegree values
result = compute_twodegree(graph)

# Print Results
print("twodegree values:")
for vertex, value in result.items():
    print(f"Vertex {vertex}: {value}")
