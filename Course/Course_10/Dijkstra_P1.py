import heapq

def dijkstra(graph, start):

    pq = []
    heapq.heappush(pq, (0, start))
    shortest_path = {node:float('inf') for node in graph}
    shortest_path[start] = 0
    while pq:
        current_dis, current_node = heapq.heappop(pq)
        if current_dis > shortest_path[current_node]:
            continue

        for neighbor, distance in graph[current_node]:
            new_dis = current_dis + distance
            if new_dis < shortest_path[neighbor]:
                shortest_path[neighbor] = new_dis
                heapq.heappush(pq, (new_dis, neighbor))

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
