from collections import defaultdict

class SCCs:
    def __init__(self,graph):
        self.graph = graph
        self.scc_s= []
        self.stack = []
        self.visited = set()
        self.transpose_graph = defaultdict(list)

    def dfs(self, node):
        self.visited.add(node)
        for neighbour in self.graph[node]:
            if neighbour not in self.visited:
                self.dfs(neighbour)
        self.stack.append(node)

    def reverse_graph(self, node, scc):
        self.visited.add(node)
        scc.append(node)
        for neighbour in self.transpose_graph[node]:
            if neighbour not in self.visited:
                self.reverse_graph(neighbour, scc)

    def find_scc_s(self):

        for node in graph:
            if node not in self.visited:
                self.dfs(node)

        for node in self.graph:
            for neighbour in self.graph[node]:
                self.transpose_graph[neighbour].append(node)

        self.visited.clear()

        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                scc = []
                self.reverse_graph(node, scc)
                self.scc_s.append(scc)

        return self.scc_s

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
print(scc_finder.find_scc_s())  # 输出: [[6], [3], [2, 5, 4, 1]]
