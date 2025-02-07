# class GraphAdjList:
#     def __init__(self, vertices):
#         self.vertices = vertices
#         self.adj_list = {i: [] for i in range(vertices)}  # Initialize adjacency list
#
#     # Add an edge for directed graph
#     def add_edge(self, src, dest):
#         self.adj_list[src].append(dest)
#
#     # Add an edge for undirected graph
#     def add_undirected_edge(self, src, dest):
#         self.adj_list[src].append(dest)
#         self.adj_list[dest].append(src)
#
#     # Display the adjacency list
#     def display(self):
#         for node, neighbors in self.adj_list.items():
#             print(f"Node {node}: {neighbors}")

class GraphAdjList():
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {i : [] for i in range(vertices)}

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)

    def display(self):
        for node, neighbors in self.adjacency_list.items():
            print(f"{node} -> {neighbors}")





# Example usage
if __name__ == "__main__":
    graph = GraphAdjList(5)  # Create a graph with 5 nodes (0 to 4)

    # Add edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(3, 4)

    # Display the graph
    graph.display()
