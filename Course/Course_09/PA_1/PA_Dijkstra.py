import heapq  # Importing heapq for priority queue (min-heap)
from collections import defaultdict  # Importing defaultdict for adjacency list representation

class Graph:
    def __init__(self, graph):
        """
        Initialize the graph.
        :param graph: A dictionary representing an adjacency list {node: [(neighbor, weight), ...]}
        """
        self.graph = graph

    def dijkstra_shortest_cycle(self, start):
        """
        Uses Dijkstra's algorithm to find the shortest cycle starting and ending at 'start'.
        :param start: The node from which to start searching for a cycle.
        :return: Length of the shortest cycle if found, otherwise None.
        """
        shortest_cycle = {node: float('inf') for node in self.graph}  # Initialize distances with infinity
        shortest_cycle[start] = 0  # Distance to start node is 0
        pq = [(shortest_cycle[start], start)]  # Priority queue (min-heap) initialized with start node

        while pq:
            current_dis, current_node = heapq.heappop(pq)  # Get the node with the smallest distance

            if current_node in self.graph:
                for neighbor, weight in self.graph[current_node]:  # Iterate through all neighbors
                    new_dis = current_dis + weight  # Calculate new distance

                    # Ensure we detect a valid cycle (must not be a direct back edge)
                    if neighbor == start and current_node != start:
                        return new_dis  # Return the length of the cycle found

                    # Update shortest paths and add to priority queue if beneficial
                    if neighbor not in shortest_cycle or new_dis < shortest_cycle[neighbor]:
                        shortest_cycle[neighbor] = new_dis
                        heapq.heappush(pq, (new_dis, neighbor))

        return None  # If no cycle is found, return None

    def finding_shortest_cycle(self):
        """
        Finds the shortest cycle in the entire graph by checking cycles from every node.
        :return: The length of the shortest cycle found, or 0 if no cycles exist.
        """
        if len(self.graph) <= 1:
            return 0  # A single-node graph has no cycles

        shortest_dis = float('inf')  # Initialize the shortest cycle distance as infinity

        for start in self.graph:  # Iterate over all nodes as potential starting points
            dis = self.dijkstra_shortest_cycle(start)  # Find shortest cycle from this node
            if dis is not None and dis < shortest_dis:
                shortest_dis = dis  # Update shortest cycle length if a shorter one is found

        return shortest_dis if shortest_dis != float('inf') else 0  # Return 0 if no cycles exist

# Initialize an empty graph using a dictionary with lists as default values
graph = defaultdict(list)

# Read the graph structure from a file
with open("testcase-4.txt", "r") as file:  # Open the input file
    for line in file:
        parts = line.strip().split(" : ")  # Split the line into vertex and its neighbors
        if len(parts) < 2:
            continue  # Skip invalid lines
        u = int(parts[0])  # Extract the source vertex
        edges = parts[1].split()  # Split the neighbor and weight pairs

        # Parse the neighbor nodes and their respective weights
        for i in range(0, len(edges), 2):
            v = int(edges[i])  # Neighbor vertex
            l = int(edges[i + 1])  # Edge weight
            graph[u].append((v, l))  # Add edge to adjacency list

# Create a graph object
g = Graph(graph)

# Run the shortest cycle detection algorithm
shortest_cycle_test_case = g.finding_shortest_cycle()

# Print the result
print("The length of the shortest cycle is:", shortest_cycle_test_case)
