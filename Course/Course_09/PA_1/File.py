from collections import defaultdict  # Importing defaultdict for adjacency list representation

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

if __name__ == "__main__":

    gr = read_graph_from_file("testcase-8.txt")
    for node, neighbors in gr.items():
        print(f"Node {node} has neighbors: {neighbors}")