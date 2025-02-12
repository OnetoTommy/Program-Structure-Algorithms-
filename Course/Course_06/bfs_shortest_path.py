from collections import deque


def bfs_shortest_path(graph, start):
    # Initialize distances to infinity and previous nodes to None
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    a = []

    # Initialize queue and set distance of start node to 0
    queue = deque([start])
    dist[start] = 0

    while queue:
        u = queue.popleft()  # Dequeue a node
        a.append(u)
        for v in graph[u]:  # Iterate over its neighbors
            if dist[v] == float('inf'):  # If v is unvisited

                dist[v] = dist[u] + 1  # Update distance
                prev[v] = u  # Store previous node
                queue.append(v)  # Enqueue v

    return dist, a  # Return shortest distances and previous nodes


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

# Run BFS from node 'A'
distances, predecessors = bfs_shortest_path(graph, 'A')

# Print results
print("Shortest distances:", distances)
print("Predecessors:", predecessors)
