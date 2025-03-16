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
        for neighbor, weight in self.reverse_graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)
        self.stack.append(node)
    def orginal_dfs(self, node, scc):
        self.visited.add(node)
        scc.append(node)
        for neighbor, weight in self.graph[node]:
            if neighbor not in self.visited:
                self.orginal_dfs(neighbor, scc)

    def find_sccs(self):
        self.reverse_graph.clear()
        self.visited.clear()
        self.stack.clear()
        self.SCCs.clear()

        edges_to_add = []
        for node in self.graph:
            for neighbors, weight in self.graph[node]:
                edges_to_add.append((neighbors, node, weight))

        for neighbors, node, weight in edges_to_add:
            self.reverse_graph[neighbors].append((node, weight))

        for node in list(self.reverse_graph):
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

# # Example Usage
# graph = {
#     1: [(2,1)],
#     2: [(3, 1), (5,1)],
#     3: [(6,1)],
#     4: [(1,1)],
#     5: [(4,1)],
#     6: []
# }
# graph = {
#     0: [(1,1)],
#     1: [(2, 2)],
#     2: [(3,3)],
#     3: [(1,4), (0,5)],
#
# }
#
#
# scc_finder = SCC(graph)
# print(scc_finder.find_sccs())  # 输出: [[6], [3], [2, 5, 4, 1]]