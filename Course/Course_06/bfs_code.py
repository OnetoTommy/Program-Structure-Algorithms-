from collections import deque

def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = deque([start])  # Initialize the queue with the starting node

    while queue:
        node = queue.popleft()  # Dequeue a node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark it as visited
            queue.extend(graph[node])  # Enqueue all its adjacent nodes

# Example graph (Adjacency List)
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

# Run BFS starting from node 'A'
bfs(graph, 'A')
