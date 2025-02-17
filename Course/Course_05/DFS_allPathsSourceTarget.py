def allPathsSourceTarget(graph):
    a = list()
    b = list()
    def pathSource(x):
        n = len(graph) - 1
        if x == n:
            a.append(b[:])
            return
        for i in graph[x]:
            b.append(i)
            pathSource(i)
            b.pop()

    b.append(0)
    pathSource(0)
    return a

graph = [[1, 2], [3], [3], []]
result = allPathsSourceTarget(graph)
print(result)
