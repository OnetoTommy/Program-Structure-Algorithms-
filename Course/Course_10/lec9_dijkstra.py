import heapq

class Graph:
    def __init__(self, numV):
        self.numV = numV
        ## To store edge weights
        self.adj = [[] for _ in range(numV)]

    def add_edge(self, u, v, l):
        self.adj[u].append((v, l))
        self.adj[v].append((u, l))

    def dijkstra_shortest_path(self, src):
        # Priority queue (pq) to store vertices being preprocessed
        # (weight, vertex)
        
 
        # Initialize all distances as infinite (INF)
        dist = [float('inf')] * self.numV
        dist[src] = 0
        pq = [(dist[src], src)]
 
        # Looping until the pq becomes empty
        while pq:
            # Extract the vertex with min weight from the pq
            current_dist, u = heapq.heappop(pq)
 
            # Iterate over all adjacent vertices of a vertex
            for v, weight in self.adj[u]:
                # If there is a shorter path to v through u
                if dist[v] > dist[u] + weight:
                    # Update the distance of v
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
 
        # Print shortest distances
        print("Vertex Distance from Source")
        for i in range(self.numV):
            print(f"{i}\t\t{dist[i]}")

if __name__ == "__main__":

    ex = 2

    if ex == 1:
        V = 9
        g = Graph(V)
 
        g.add_edge(0, 1, 4)
        g.add_edge(0, 7, 8)
        g.add_edge(1, 2, 8)
        g.add_edge(1, 7, 11)
        g.add_edge(2, 3, 7)
        g.add_edge(2, 8, 2)
        g.add_edge(2, 5, 4)
        g.add_edge(3, 4, 9)
        g.add_edge(3, 5, 14)
        g.add_edge(4, 5, 10)
        g.add_edge(5, 6, 2)
        g.add_edge(6, 7, 1)
        g.add_edge(6, 8, 8)
        g.add_edge(7, 8, 7)

        src = 0
    
    if ex == 2:
        V = 4
        g = Graph(V)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 8)
        g.add_edge(1, 2, 9)
        g.add_edge(1, 3, 2)
        g.add_edge(2, 3, 6)

        src = 0



    g.dijkstra_shortest_path(src)

