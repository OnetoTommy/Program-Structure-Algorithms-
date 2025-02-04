def dfs(graph, v, visited=None, parent=None):
    if visited is None:
        visited = set()
    if parent is None:
        parent = {}

    visited.add(v)  # Mark v as visited
    print(f"Visited: {v}")

    for w in graph[v]:  # Iterate over neighbors
        if w not in visited:
            parent[w] = v  # Track the parent (w.prev = v)
            dfs(graph, w, visited, parent)

    return parent  # Return parent mapping

# Example Graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Start DFS from 'A'
parent_map = dfs(graph, 'A')

# Print the parent mapping
print("\nParent mapping (prev):")
for node, prev in parent_map.items():
    print(f"{node} ← {prev}")  # w.prev ← v
