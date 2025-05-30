import heapq  # Importing heapq for priority queue (min-heap)
import argparse  # Importing argparse to handle command-line arguments
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
        # Priority queue entries are tuples of (distance, current_node)
        pq = [(0, start)]
        # Distance dictionary stores shortest known distance to each node
        distances = {start: 0}
        # Keep track of visited nodes to avoid revisiting
        visited = set()
        parent = {start: None}  # To track the parent of each node for cycle detection

        while pq:
            dist, current_node = heapq.heappop(pq)

            # Skip if we've already processed this node
            if current_node in visited:
                continue

            # Check for cycle: if we revisit the start node and it's not a direct back edge
            if current_node == start and dist > 0:
                return dist

            visited.add(current_node)

            # For each neighbor and weight from current node
            for neighbor, weight in self.graph.get(current_node, []):
                if neighbor in visited:
                    # If we find a path back to start_node, it's a cycle
                    if neighbor == start and current_node != parent[start]:
                        return dist + weight
                    continue

                new_dist = dist + weight
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    parent[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))

        return None  # If no cycle is found

    def finding_shortest_cycle(self):
        """
        Finds the shortest cycle in the entire graph by checking cycles from every node.
        :return: The length of the shortest cycle found, or 0 if no cycles exist.
        """
        if len(self.graph) <= 1:
            return 0  # A single-node graph has no cycles

        shortest_cycle = float('inf')  # Initialize the shortest cycle distance as infinity

        for start in self.graph:  # Iterate over all nodes as potential starting points
            cycle_length = self.dijkstra_shortest_cycle(start)  # Find shortest cycle from this node
            if cycle_length is not None and cycle_length < shortest_cycle:
                shortest_cycle = cycle_length  # Update shortest cycle length if a shorter one is found

        return shortest_cycle if shortest_cycle != float('inf') else 0  # Return 0 if no cycles exist


def read_graph_from_file(file_name):
    graph_data = defaultdict(list)

    with open(file_name, "r") as file:
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
                graph_data[u].append((v, l))  # Add edge to adjacency list

    return graph_data


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Find the shortest cycle in a graph")
    parser.add_argument('-input', type=str, required=True, help="Input graph file")
    args = parser.parse_args()

    # Read the graph from the input file
    graph = read_graph_from_file(args.input)

    # Create a graph object
    g = Graph(graph)

    # Run the shortest cycle detection algorithm
    shortest_cycle_test_case = g.finding_shortest_cycle()

    # Print the result
    print("The length of the shortest cycle is:", shortest_cycle_test_case)


if __name__ == "__main__":
    main()
