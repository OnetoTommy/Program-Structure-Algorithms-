from collections import defaultdict



class SCC:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.reverse_graph = defaultdict(list)
        self.SCCs = []
        self.stack = []

    def dfs(self, node):
        self.visited.add(node)
        for neighbor in self.reverse_graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.stack.append(node)
    def orginal_dfs(self, node, scc):
        self.visited.add(node)
        scc.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.orginal_dfs(neighbor, scc)
    def find_sccs(self):
        for node in self.graph:
            for neighbors in self.graph[node]:
                self.reverse_graph[neighbors].append(node)

        for node in self.reverse_graph:
            if node not in self.visited:
                self.dfs(node)

        self.visited.clear()

        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                scc = []
                self.orginal_dfs(node, scc)
                self.SCCs.append(scc)
        return self.SCCs


# Example Usage
graph = {
    1: [2],
    2: [3, 5],
    3: [6],
    4: [1],
    5: [4],
    6: []
}

scc_finder = SCC(graph)
print(scc_finder.find_sccs())  # 输出: [[6], [3], [2, 5, 4, 1]]