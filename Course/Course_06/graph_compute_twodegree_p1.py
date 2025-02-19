def c_two_degree(graph):

    degree = {}
    two_degree = {}


    for v, neighbors in graph.items():
        degree[v] = len(neighbors)

    for v, neighbors in graph.items():
        sum = 0
        for u in neighbors:
            sum += degree[u]
        two_degree[v] = sum

    return two_degree

graph = {
    1: [2, 3],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [3, 5],
    5: [3, 4, 6],
    6: [5]
}

# Compute twodegree values
result = c_two_degree(graph)

# Print Results
print("twodegree values:")
for vertex, value in result.items():
    print(f"Vertex {vertex}: {value}")