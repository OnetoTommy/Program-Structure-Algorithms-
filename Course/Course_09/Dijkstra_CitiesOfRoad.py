import heapq


class Graph:
    def __init__(self, numV):
        self.numV = numV
        # Adjacency list to store edge weights
        self.adj = [[] for _ in range(numV)]

    def add_edge(self, u, v, length):
        # Add edge from u to v with weight length
        self.adj[u].append((v, length))

    def dijkstra(self, src):
        # Initialize all distances as infinite
        dist = [float('inf')] * self.numV
        dist[src] = 0
        pq = [(0, src)]  # Priority queue initialized with source vertex

        while pq:
            current_dist, u = heapq.heappop(pq)

            for v, weight in self.adj[u]:
                # Relax the edge if a shorter path is found
                if dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))  # Push the updated distance to the queue
        return dist

    def find_max_decrease(self, s, t, potential_roads):
        # Step 1: Run Dijkstra's algorithm from source s
        dist_s = self.dijkstra(s)

        # Step 2: Run Dijkstra's algorithm from destination t
        dist_t = self.dijkstra(t)

        # Step 3: Evaluate each potential road e'
        max_decrease = 0
        best_road = None

        for u, v, length in potential_roads:
            # Calculate the new distance from s to t with the potential road
            new_dist = min(dist_s[u] + length + dist_t[v], dist_s[v] + length + dist_t[u])
            decrease = dist_s[t] - new_dist

            if decrease > max_decrease:
                max_decrease = decrease
                best_road = (u, v, length)

        return best_road, max_decrease


# Example usage:
if __name__ == "__main__":
    V = 5  # Number of cities
    g = Graph(V)

    # Adding existing roads (edges) with associated lengths
    g.add_edge(0, 1, 6)
    g.add_edge(0, 4, 1)
    g.add_edge(1, 2, 5)
    g.add_edge(1, 4, 2)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 7)

    # List of potential roads with their lengths (u, v, length)
    potential_roads = [(0, 2, 3), (1, 3, 4), (2, 4, 1)]

    s, t = 0, 3  # Fixed cities s and t
    best_road, max_decrease = g.find_max_decrease(s, t, potential_roads)

    print(f"Best road to add: {best_road}")
    print(f"Maximum decrease in distance: {max_decrease}")
