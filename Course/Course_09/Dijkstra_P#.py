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
        for neighbor, distance in graph[current_node]:
            new_dist = current_dist + distance
            if new_dist < shortest_path[neighbor]:
                shortest_path[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return shortest_path


graph = {
    'A': [('B', 1)],
    'B': [('C', 2)],
    'C': [('D', 10)],
    'D': [('B', 5)]
}

# Run Dijkstra’s Algorithm from node 'A'
shortest_paths = dijkstra(graph, 'A')
print("Shortest distances from A:", shortest_paths)