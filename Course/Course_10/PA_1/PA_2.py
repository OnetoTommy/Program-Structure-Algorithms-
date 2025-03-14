import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_Direct_Edge(self, u, v, l):
        """Adds a directed edge from u to v with weight l."""
        self.graph[u].append((v, l))

    def dijkstra_shortest_cycle(self, start):

        shortest_cycle = {node:float('inf') for node in self.graph}
        shortest_cycle[start] = 0
        pq = [(shortest_cycle[start], start)]
        while pq:
            current_dis, current_node = heapq.heappop(pq)

            if current_node in self.graph:
                for neighbor, weight in self.graph[current_node]:
                    new_dis = current_dis + weight
                    #Ensure valid cycle (must not be a direct back edge)
                    if neighbor == start and current_node != start:
                        return new_dis  # Return valid cycle length

                    if neighbor not in shortest_cycle or new_dis < shortest_cycle[neighbor]:  # Only update if beneficial
                        shortest_cycle[neighbor] = new_dis
                        heapq.heappush(pq, (new_dis, neighbor))
        return None


    def finding_shortest_cycle(self):
        if len(self.graph) <= 1:
            return 0

        shortest_dis = float('inf')
        for start in self.graph:
            dis = self.dijkstra_shortest_cycle(start)
            if dis is not None and dis < shortest_dis:
                shortest_dis = dis

        return shortest_dis if shortest_dis != float('inf') else 0

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
shortest_cycle_test_case = g.finding_shortest_cycle()
print("The length of the shortest cycle is:", shortest_cycle_test_case)