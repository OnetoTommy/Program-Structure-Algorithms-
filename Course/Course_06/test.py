from collections import defaultdict

class SCCs:
    def __init__(self, graph):
        self.graph = graph
        self.scc_s = []
        self.stack = []
        self.visited = set()
        self.transpose_graph = defaultdict(list)

    def dfs(self, node):
        """Regular DFS on the original graph, used to fill the stack with finish times."""
        self.visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.stack.append(node)

    def reverse_graph_dfs(self, node, scc):
        """
        DFS on the transposed graph.
        Appends the node to the current strongly connected component (scc).
        """
        self.visited.add(node)
        scc.append(node)  # Add the current node to the SCC
        for neighbor in self.transpose_graph[node]:
            if neighbor not in self.visited:
                self.reverse_graph_dfs(neighbor, scc)

    def find_scc_s(self):
        """
        1) DFS on original graph to get a finishing-time stack.
        2) Transpose the graph.
        3) Pop nodes from stack and DFS on the transposed graph to get SCCs.
        """
        # Step 1: DFS on original graph
        for node in self.graph:
            if node not in self.visited:
                self.dfs(node)

        # Step 2: Clear visited and build the transposed graph
        self.visited.clear()
        for node in self.graph:
            for neighbor in self.graph[node]:
                # Append the original 'node' to the adjacency list of 'neighbor'
                # in the transposed graph
                self.transpose_graph[neighbor].append(node)

        # Step 3: Pop from stack and DFS on transposed graph
        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                scc = []
                self.reverse_graph_dfs(node, scc)
                self.scc_s.append(scc)

        return self.scc_s


# Example Usage
if __name__ == "__main__":
    graph = {
        1: [2],
        2: [3, 5],
        3: [6],
        4: [1],
        5: [4],
        6: []
    }

    scc_finder = SCCs(graph)
    print(scc_finder.find_scc_s())  # Expected: [[6], [3], [2, 5, 4, 1]]
