from collections import defaultdict

class SCCFinder:
    def __init__(self, graph):
        self.graph = graph
        self.transposed_graph = defaultdict(list)
        self.visited = set()
        self.stack = []
        self.sccs = []

    def dfs(self, node):
        self.visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)  
        self.stack.append(node)

    def reverse_dfs(self, node, scc):
        self.visited.add(node)
        scc.append(node)
        for neighbor in self.transposed_graph[node]:
            if neighbor not in self.visited:
                self.reverse_dfs(neighbor, scc)

    def find_sccs(self):
        # Step 1: Perform DFS and store finish times
        for node in self.graph:
            if node not in self.visited:
                self.dfs(node)

        # Step 2: Transpose the graph
        for node in self.graph:
            for neighbor in self.graph[node]:
                self.transposed_graph[neighbor].append(node)

        # Step 3: Process nodes in decreasing finish order
        self.visited.clear()
        while self.stack:
            node = self.stack.pop()
            if node not in self.visited:
                scc = []
                self.reverse_dfs(node, scc)
                self.sccs.append(scc)

        return self.sccs

# Example Usage
graph = {
    'a': ['b','c','d','f'],
    'b': ['d'],
    'c': ['d', 'e'],
    'd': ['e','f'],
    'e': ['a','f'],
    'f': [],
    'g': ['b','h'],
    'h': ['d']
}

scc_finder = SCCFinder(graph)
print(scc_finder.find_sccs())  # 输出: [[6], [3], [2, 5, 4, 1]]
