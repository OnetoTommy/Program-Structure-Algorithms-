import  heapq

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    shortest_path = {node:float('inf') for node in graph}
    shortest_path[start] = 0
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > shortest_path[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight
            if new_dist < shortest_path[neighbor]:
                shortest_path[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return shortest_path

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Run Dijkstra’s Algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from A:", shortest_paths)