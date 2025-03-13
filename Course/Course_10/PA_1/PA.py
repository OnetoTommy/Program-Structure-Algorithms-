import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_Direct_Edge(self, u, v, l):
        """Adds a directed edge from u to v with weight l."""
        self.graph[u].append((v, l))

    def tarjan_scc(self):
        """Finds all SCCs using Tarjan's Algorithm."""
        self.index = 0
        self.stack = []
        self.index_map = {}  # Node -> Index
        self.low_link = {}  # Node -> Low Link Value
        self.on_stack = set()
        self.sccs = []

        def strongconnect(node):
            self.index_map[node] = self.low_link[node] = self.index
            self.index += 1
            self.stack.append(node)
            self.on_stack.add(node)

            for neighbor, _ in self.graph[node]:
                if neighbor not in self.index_map:
                    strongconnect(neighbor)
                    self.low_link[node] = min(self.low_link[node], self.low_link[neighbor])
                elif neighbor in self.on_stack:
                    self.low_link[node] = min(self.low_link[node], self.index_map[neighbor])

            if self.low_link[node] == self.index_map[node]:
                scc = []
                while True:
                    n = self.stack.pop()
                    self.on_stack.remove(n)
                    scc.append(n)
                    if n == node:
                        break
                self.sccs.append(scc)

        for node in list(self.graph):  # Fix: Convert keys to a list to prevent runtime modification issues
            if node not in self.index_map:
                strongconnect(node)

        return self.sccs

    def dijkstra_Shortest_Cycle(self):
        """Finds the shortest cycle within each SCC using Dijkstra."""
        shortest_len = float('inf')
        scc_finder = self.tarjan_scc()

        # Remove single-node SCCs (which have no cycles)
        scc_finder = [scc for scc in scc_finder if len(scc) > 1]
        if not scc_finder:
            return 0  # No cycles in the graph

        for scc in scc_finder:
            scc_set = set(scc)  # Convert SCC list to a set for fast lookup

            for start in scc:
                # Run Dijkstra from each node in SCC
                pq = [(0, start)]  # Min heap (distance, node)
                distances = {node: float('inf') for node in scc}
                distances[start] = 0

                while pq:
                    current_distance, current_node = heapq.heappop(pq)

                    if current_distance > distances[current_node]:
                        continue  # Ignore outdated distances

                    for neighbor, weight in self.graph[current_node]:
                        if neighbor in scc_set:  # Only process nodes inside SCC
                            new_distance = distances[current_node] + weight
                            if new_distance < distances[neighbor]:
                                distances[neighbor] = new_distance
                                heapq.heappush(pq, (new_distance, neighbor))

                # Check for the shortest cycle by considering all paths returning to `start`
                for node in scc:
                    for neighbor, weight in self.graph[node]:  # Edge from node → neighbor
                        if neighbor == start:  # Direct return edge to start
                            cycle_length = distances[node] + weight
                            shortest_len = min(shortest_len, cycle_length)

        return shortest_len if shortest_len != float('inf') else 0

if __name__ == "__main__":

    ex = 6

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
    if ex == 4:
        g = Graph()
        g.add_Direct_Edge(0, 1, 1)
        g.add_Direct_Edge(1, 2, 2)
        g.add_Direct_Edge(2, 3, 3)
        g.add_Direct_Edge(3, 1, 4)
        g.add_Direct_Edge(3, 0, 5)
    if ex == 5:
        g = Graph()
        g.add_Direct_Edge(0, 1, 1)
        g.add_Direct_Edge(0, 2, 4)
        g.add_Direct_Edge(1, 3, 2)
        g.add_Direct_Edge(2, 3, 1)
        g.add_Direct_Edge(3, 0, 3)
    if ex == 6:
        g = Graph()
        g.add_Direct_Edge(0, 1, 1)
        g.add_Direct_Edge(1, 2, 2)
        g.add_Direct_Edge(2, 3, 3)

# Run the shortest cycle detection algorithm on the new test case
shortest_cycle_test_case = g.dijkstra_Shortest_Cycle()
print("Shortest cycle length:", shortest_cycle_test_case)