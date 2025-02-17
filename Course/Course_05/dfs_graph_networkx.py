import networkx as nx
import matplotlib.pyplot as plt

# 创建一个无向图
G = nx.Graph()

# 添加节点
G.add_nodes_from([1, 2, 3, 4, 5])

# 添加边
G.add_edges_from([(1, 2), (2, 3), (4, 5)])

# 打印节点和边
print("Nodes:", G.nodes())  # 输出: Nodes: [1, 2, 3, 4, 5]
print("Edges:", G.edges())  # 输出: Edges: [(1, 2), (2, 3), (4, 5)]


nx.draw_networkx(G)
plt.show()
