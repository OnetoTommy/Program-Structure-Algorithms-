class AdjacencyMatrix:
    def __init__(self, node):
        self.node = node
        self.adjacency_matrix = [[0] * node for _ in range(node)]

    def add_edge(self, v, u):
        self.adjacency_matrix[v][u] = 1

    def add_undirected_edge(self, src, dest):
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1

    def display(self):
        for i in self.adjacency_matrix:
            print(i)

if __name__ == "__main__":
    graph = AdjacencyMatrix(5)
    graph.add_undirected_edge(0, 1)
    graph.add_undirected_edge(0, 4)
    graph.add_undirected_edge(1, 2)
    graph.add_undirected_edge(1, 3)
    graph.add_undirected_edge(1, 4)
    graph.add_undirected_edge(3, 4)

    graph.display()