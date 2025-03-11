import heapq


def dijkstra(graph, start):
    """
    Implements Dijkstra's Algorithm to find the shortest path from a single source node.

    :param graph: Dictionary where keys are nodes and values are lists of (neighbor, weight) pairs.
    :param start: The starting node.
    :return: Dictionary with shortest distances from start to all other nodes.
    """
    # Priority queue (min-heap)
    pq = []
    heapq.heappush(pq, (0, start))  # (distance, node)

    # Dictionary to store the shortest known distances
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)

        # If the current distance is greater than the recorded shortest distance, skip processing
        if current_distance > shortest_distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_distances


# Example Graph Representation (Adjacency List)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Run Dijkstra’s Algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from A:", shortest_paths)
