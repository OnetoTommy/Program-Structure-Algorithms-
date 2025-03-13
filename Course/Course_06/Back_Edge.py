from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def has_cycle_util(self, node, visited, recursion_stack):
        """DFS-based cycle detection in a directed graph."""
        visited[node] = 1  # Mark node as being visited (Gray)
        recursion_stack[node] = 1  # Track recursion stack

        for neighbor in self.graph[node]:
            if visited[neighbor] == 0:  # White node, explore deeper
                if self.has_cycle_util(neighbor, visited, recursion_stack):
                    return True
            elif recursion_stack[neighbor] == 1:  # If already in recursion stack → cycle detected
                return True

            recursion_stack[node] = 0  # Remove from recursion stack (Black)
        return False

    def has_cycle(self):
        """Check if the graph has a cycle."""
        visited = {node: 0 for node in self.graph}  # White: Not visited
        recursion_stack = {node: 0 for node in self.graph}  # Track recursion stack

        for node in self.graph:
            if visited[node] == 0:  # If not visited, start DFS
                if self.has_cycle_util(node, visited, recursion_stack):
                    return True
        return False

# Example 1: Graph Without Cycle
g1 = Graph()
g1.add_edge(1, 2)
g1.add_edge(2, 3)
g1.add_edge(3, 4)
g1.add_edge(4, 5)
g1.add_edge(5, 6)

print("Graph 1 has cycle?", g1.has_cycle())  # Output: False

# Example 2: Graph With Cycle
g2 = Graph()
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(3, 4)
g2.add_edge(4, 5)
g2.add_edge(5, 6)
g2.add_edge(6, 3)  # Cycle: 3 → 4 → 5 → 6 → 3