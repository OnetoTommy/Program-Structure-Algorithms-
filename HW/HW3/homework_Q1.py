import networkx
import networkx as nx
import matplotlib.pyplot as plt

from Course.Course_06.graph_compute_twodegree import vertex

# Create a directed graph
G = nx.DiGraph()

# Add the edges based on the DFS intervals (pre/post) and logical connections
# Add nodes (optional as they are added automatically with edges)
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8])

# Add directed edges
G.add_edges_from([(7, 6), (6, 5), (5, 1), (5, 2), (8, 4), (8, 3)])

# Draw the directed graph
plt.figure(figsize=(16, 12))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=1500, font_size=14, arrows=True)
plt.title("Directed Graph G", fontsize=16)
plt.show()
