def connected_components(graph):
    visited = set()
    components = {}
    ccnums=0

    def explore(v):
        visited.add(v)
        components[v] = ccnums
        for neighbor in graph[v]:
            if neighbor not in visited:
                explore(neighbor)

    for v in graph:
        if v not in visited:
            ccnums+=1
            explore(v)

    return components

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E']
}

# Find connected components
result = connected_components(graph)
print(result)