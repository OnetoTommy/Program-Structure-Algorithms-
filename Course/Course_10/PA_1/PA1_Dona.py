import heapq
import sys

def read_graph_from_file(file_name):

    graph_data = {}
    malformed_lines = []  # Stores lines with incorrect format

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Handle empty file
            if not lines:
                print("Error: The input file is empty.")
                sys.exit(1)

            for line in lines:
                parts = line.strip().split(':')  # Split by ':', e.g., ["0", "1 3 2 5"]
                if len(parts) != 2:
                    malformed_lines.append(line.strip())  # Record malformed lines
                    continue

                try:
                    source = int(parts[0].strip())  # Extract the source node
                except ValueError:
                    print(f"Error: Invalid vertex name in line: {line.strip()}")
                    sys.exit(1)

                edges = parts[1].strip().split()  # Read edges and weights
                if len(edges) % 2 != 0:
                    print(f"Error: Edge list in line '{line.strip()}' is malformed.")
                    sys.exit(1)

                # Initialize adjacency list if source node is new
                if source not in graph_data:
                    graph_data[source] = []

                for i in range(0, len(edges), 2):
                    try:
                        dest = int(edges[i])
                        weight = int(edges[i + 1])

                        if weight <= 0:
                            print(f"Error: Edge weight must be positive in line: {line.strip()}")
                            sys.exit(1)  # Ensure program exits on negative weights

                        graph_data[source].append((dest, weight))
                    except ValueError:
                        print(f"Error: Edge weight should be a number: {line.strip()}")
                        sys.exit(1)

        # Check if all lines were malformed
        if not graph_data:
            if malformed_lines:
                print("Error: All lines were malformed. Please check the file format.")
                for line in malformed_lines:
                    print(f" - Malformed line: {line}")
            else:
                print("Error: The graph is empty.")
            sys.exit(1)

        return graph_data

    except FileNotFoundError:
        print(f"Error: Input file '{file_name}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error reading input file: {e}")
        sys.exit(1)

def dijkstra_for_cycle(directed_graph, start_node):
    # Priority queue entries are tuples of (distance, current_node)
    pq = [(0, start_node)]
    # Distance dictionary stores shortest known distance to each node
    distances = {start_node: 0}
    # Keep track of visited nodes to avoid revisiting
    visited = set()
    
    while pq:
        dist, current = heapq.heappop(pq)
        
        # Skip if we've already processed this node
        if current in visited:
            continue
            
        # If we've found a cycle back to start_node and distance is positive
        if current == start_node and dist > 0:
            return dist
            
        visited.add(current)
            
        # For each neighbor and weight from current node
        for neighbor, weight in directed_graph.get(current, []):
            if neighbor in visited:
                # If we find a path back to start_node, it's a cycle
                if neighbor == start_node:
                    return dist + weight
                continue
                
            new_dist = dist + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                
    return float('inf')

def find_shortest_cycle(graph):
    if not graph:
        print("Error: The graph is empty.")
        sys.exit(1)

    shortest_cycle = float('inf')
    
    # Add more detailed output for debugging
    print("\nSearching for cycles starting from each vertex:")
    for node in graph:
        cycle_length = dijkstra_for_cycle(graph, node)
        if cycle_length != float('inf'):
            print(f"Found cycle of length {cycle_length} starting from vertex {node}")
        shortest_cycle = min(shortest_cycle, cycle_length)

    return shortest_cycle if shortest_cycle != float('inf') else 0

if __name__ == "__main__":
    # Ensure correct usage with an input file
    if len(sys.argv) < 2:
        print("Usage: python PA1.py <input_file>")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the input file is a .txt file
    if not filename.endswith(".txt"):
        print("Error: Input file must be a .txt file.")
        sys.exit(1)

    try:
        graph = read_graph_from_file(filename)
        shortest_cycle_length = find_shortest_cycle(graph)
        print(f"The length of the shortest cycle is: {shortest_cycle_length}")
    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except FileNotFoundError as fe:
        print(fe)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)