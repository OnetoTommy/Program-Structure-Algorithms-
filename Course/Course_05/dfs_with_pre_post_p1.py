def dfs_with_pre_post(self,graph):
    pre = {}
    post = {}
    visited = set()
    clock = [1]

    def dfs(v):
        visited.add(v)
        pre[v] = clock[0]
        clock[0] += 1
        for w in graph[v]:
            if w not in visited:
                dfs(w)

        post[v] = clock[0]
        clock[0] += 1

    for v in graph:
        if v not in visited:
            dfs(v)

    return pre, post

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

# Run DFS and get timestamps
pre, post = dfs_with_pre_post(graph)
print("Pre-order:", pre)
print("Post-order:", post)


