import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_Direct_Edge(self, u, v, l):
        """Adds a directed edge from u to v with weight l."""
        self.graph[u].append((v, l))

    def dijkstra_shortest_cycle(self, start):
        """Finds the shortest cycle that includes the start node using Dijkstra's algorithm."""
        shortest_cycle = defaultdict(lambda: float('inf'))  # ✅ Auto-initialize missing nodes
        shortest_cycle[start] = 0
        pq = [(0, start)]  # ✅ Start with distance 0

        while pq:
            current_dis, current_node = heapq.heappop(pq)

            if current_node in self.graph:
                for neighbor, weight in self.graph[current_node]:
                    new_dis = current_dis + weight

                    # ✅ Ensure valid cycle (must not be a direct back edge)
                    if neighbor == start and current_node != start:
                        return new_dis  # ✅ Return valid cycle length

                    if new_dis < shortest_cycle[neighbor]:  # ✅ Only update if beneficial
                        shortest_cycle[neighbor] = new_dis
                        heapq.heappush(pq, (new_dis, neighbor))

        return None  # ✅ Return None if no cycle is found

    def finding_shortest_cycle(self):
        """Finds the shortest cycle in the graph by trying all nodes as start points."""
        if len(self.graph) <= 1:
            return 0  # ✅ No cycles possible

        shortest_dis = float('inf')

        for start in self.graph:
            dis = self.dijkstra_shortest_cycle(start)
            if dis is not None and dis < shortest_dis:
                shortest_dis = dis

        return shortest_dis if shortest_dis != float('inf') else 0  # ✅ Return 0 if no cycles exist

# ✅ Test Cases
if __name__ == "__main__":
    g = Graph()
    g.add_Direct_Edge(0, 1, 1)
    g.add_Direct_Edge(1, 2, 2)
    g.add_Direct_Edge(2, 3, 3)
    g.add_Direct_Edge(3, 1, 4)  # ✅ Forms a cycle: 1 → 2 → 3 → 1

    # Run shortest cycle detection
    shortest_cycle_test_case = g.finding_shortest_cycle()
    print("The length of the shortest cycle is:", shortest_cycle_test_case)
