import networkx as nx
import matplotlib.pyplot as plt

# Define the directed graph edges from the problem statement
graph_edges = {
    1: [4, 5],
    2: [7, 8],
    3: [12, 13],
    4: [14, 15],
    5: [3, 6],
    6: [2, 9],
    7: [1, 10],
    8: [11, 16]
}

G = nx.DiGraph()

for fromV, toUs in graph_edges.items():
    for toU in toUs:
        G.add_edge(fromV, toU)

nx.draw_networkx(G)
plt.figure(figsize=(8, 6))

plt.title("Directed Graph Representation")
plt.show()