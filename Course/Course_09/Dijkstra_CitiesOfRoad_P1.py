import heapq



class Solution:
    def __init__(self, cities):
        self.cities = cities
        self.adj = [[] for _ in range(self.cities)]

    def add_edge(self, u, v, l):
        self.adj[u].append((v, l))

    def dijkstra(self, start):
        adj_pq = [float("inf")] * self.cities
        adj_pq[start]=0
        pq = [(0, start)]
        while pq:
            dis, node = heapq.heappop(pq)
            for neighbor, weight in self.adj[node]:
                new_dis = dis + weight
                if new_dis < adj_pq[neighbor]:
                    adj_pq[neighbor] = new_dis
                    heapq.heappush(pq, (new_dis, neighbor))
        return adj_pq

    def find_max_decrease(self, s, t, potential_cities):
        dist_s = self.dijkstra(s)
        dist_t = self.dijkstra(t)
        max_deceased= 0
        best_road = None
        for u, v, l in potential_cities:
            max_dist = min(dist_s[u] + l + dist_t[v], dist_t[v] + dist_s[u] + l)
            decrease = dist_s[t] - max_dist
            if decrease > max_deceased:
                max_deceased = decrease
                best_road = (u, v, l)
        return best_road, max_deceased

# Example usage:
if __name__ == "__main__":
    V = 5  # Number of cities
    g = Solution(V)

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