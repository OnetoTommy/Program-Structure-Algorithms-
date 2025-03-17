import heapq
from SCC import SCC
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.scc = SCC(self.graph)

    def add_Direct_Edge(self, u, v, l):  # Create add directed edge instance
        self.graph[u].append((v, l))

    # def find_sccs(self):
    #     scc_finder = SCC(self.graph)  # Create SCC instance after edges are added
    #     return scc_finder.find_sccs()

    def dijkstra_Shortest_Path(self):
        shortest_len = float('inf')
        stack = []
        scc_s = SCC(self.graph)
        scc_finder = scc_s.find_sccs()
        # Remove single-node SCCs (which have no cycles)
        scc_finder = [scc for scc in scc_finder if len(scc) > 1]
        if not scc_finder:
            return 0  # No cycles in the graph

        for scc in scc_finder:
            scc_set = set(scc)  # Convert to set for fast lookup
            for start in scc:
                # Dijkstra’s Algorithm within SCC
                pq = [(0, start)]  # Min heap (distance, node)
                distances = {node: float('inf') for node in scc}
                distances[start] = 0
            while pq:
                current_distance, current_node = heapq.heappop(pq)
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in self.graph[current_node]:
                    if neighbor in scc_set:
                        new_distance = distances[current_node] + weight
                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
                            heapq.heappush(pq, (new_distance, neighbor))
            # Check for the shortest cycle
            for neighbor, weight in self.graph[start]:  # Edges from start
                if neighbor in scc_set and distances[neighbor] != float('inf'):
                    cycle_length = distances[neighbor] + weight
                    shortest_len = min(shortest_len, cycle_length)

        return shortest_len if shortest_len != float('inf') else 0






if __name__ == "__main__":

    ex = 4

    if ex == 1:
        g = Graph()
        g.add_Direct_Edge(0, 1, 4)
        g.add_Direct_Edge(0, 7, 8)
        g.add_Direct_Edge(1, 2, 8)
        g.add_Direct_Edge(1, 7, 11)
        g.add_Direct_Edge(2, 3, 7)
        g.add_Direct_Edge(2, 8, 2)
        g.add_Direct_Edge(2, 5, 4)
        g.add_Direct_Edge(3, 4, 9)
        g.add_Direct_Edge(3, 5, 14)
        g.add_Direct_Edge(4, 5, 10)
        g.add_Direct_Edge(5, 6, 2)
        g.add_Direct_Edge(6, 7, 1)
        g.add_Direct_Edge(6, 8, 8)
        g.add_Direct_Edge(7, 8, 7)

        src = 0
    if ex == 2:
        g = Graph()
        g.add_Direct_Edge(0, 1, 5)
        g.add_Direct_Edge(0, 2, 8)
        g.add_Direct_Edge(1, 2, 9)
        g.add_Direct_Edge(1, 3, 2)
        g.add_Direct_Edge(2, 3, 6)
        src = 0
    if ex == 3:
        g = Graph()
        g.add_Direct_Edge(1, 2, 1)
        g.add_Direct_Edge(2, 3, 1)
        g.add_Direct_Edge(2, 5, 1)
        g.add_Direct_Edge(3, 6, 1)
        g.add_Direct_Edge(4, 1, 1)
        g.add_Direct_Edge(5, 4, 1)
        src = 0
    if ex == 4:
        g = Graph()
        g.add_Direct_Edge(0, 1, 1)
        g.add_Direct_Edge(1, 2, 2)
        g.add_Direct_Edge(2, 3, 3)
        g.add_Direct_Edge(3, 1, 4)
        g.add_Direct_Edge(3, 0, 5)

        src = 0

        print(g.dijkstra_Shortest_Path())
