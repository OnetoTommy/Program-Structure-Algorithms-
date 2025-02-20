from collections import defaultdict

class SCCs:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.transpose_graph = defaultdict(list)
        self.stack = list()
        self.sccs = list()

    def dfs(self, node):
        self.visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.stack.append(node)

    def reverse_dfs(self, node, scc):
        self.visited.add(node)
        scc.append(node)
        for neighbor in self.transpose_graph[node]:
            if neighbor not in self.visited:
                self.reverse_dfs(neighbor, scc)

    def find_scc(self):
        for node in self.graph:
            if node not in self.visited:
                self.dfs(node)

        self.visited.clear()
        # transpose the graph
        for node in self.graph:
            for neighbor in self.graph[node]:
                self.transpose_graph[neighbor].append(node)


        while self.stack:
           node = self.stack.pop()
           if node not in self.visited:
               scc = []
               self.reverse_dfs(node, scc)
               self.sccs.append(scc)

        return self.sccs

# Example Usage
graph = {
    1: [2],
    2: [3, 5],
    3: [6],
    4: [1],
    5: [4],
    6: []
}

scc_finder = SCCs(graph)
print(scc_finder.find_scc())  # 输出: [[6], [3], [2, 5, 4, 1]]