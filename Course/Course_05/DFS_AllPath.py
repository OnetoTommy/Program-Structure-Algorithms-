# 给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）
#
#  graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。


class Solution():
    def __init__(self, graph):
        self.graph = graph
        self.a = list()
        self.b = list()
    def dfs(self, x:int):

        if x == len(self.graph) - 1:
            self.a.append(self.b[:])
            return

        for y in self.graph[x]:
            self.b.append(y)
            self.dfs(y)
            self.b.pop()

    def allPathsSourceTarget(self) :
        self.b.append(0)  # 从起点 0 开始
        self.dfs(0)
        return self.a





graph = [[1, 2], [3], [3], []]
solution = Solution(graph)
print(solution.allPathsSourceTarget())
