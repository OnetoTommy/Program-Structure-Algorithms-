import heapq
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra_shortest_cycle(self, start):

        shortest_cycle = {node:float('inf') for node in self.graph}
        shortest_cycle[start] = 0
        pq = [(shortest_cycle[start], start)]
        while pq:
            current_dis, current_node = heapq.heappop(pq)

            if current_node in self.graph:
                for neighbor, weight in self.graph[current_node]:
                    new_dis = current_dis + weight
                    #Ensure valid cycle (must not be a direct back edge)
                    if neighbor == start and current_node != start:
                        return new_dis  # Return valid cycle length

                    if neighbor not in shortest_cycle or new_dis < shortest_cycle[neighbor]:  # Only update if beneficial
                        shortest_cycle[neighbor] = new_dis
                        heapq.heappush(pq, (new_dis, neighbor))
        return None


    def finding_shortest_cycle(self):
        if len(self.graph) <= 1:
            return 0

        shortest_dis = float('inf')
        for start in self.graph:
            dis = self.dijkstra_shortest_cycle(start)
            if dis is not None and dis < shortest_dis:
                shortest_dis = dis

        return shortest_dis if shortest_dis != float('inf') else 0

# 初始化图
graph = defaultdict(list)

# 读取文件并解析
with open("../testcase-7.txt", "r") as file:  # 假设文件名是 graph.txt
    for line in file:
        parts = line.strip().split(" : ")  # 分割顶点与邻居
        if len(parts) < 2:
            continue
        u = int(parts[0])  # 当前顶点
        edges = parts[1].split()  # 获取所有目标节点和权重

        # 解析邻居节点及权重
        for i in range(0, len(edges), 2):
            v = int(edges[i])
            l = int(edges[i + 1])
            graph[u].append((v, l))  # 添加到字典

g = Graph(graph)
shortest_cycle_test_case = g.finding_shortest_cycle()
print("The length of the shortest cycle is:", shortest_cycle_test_case)