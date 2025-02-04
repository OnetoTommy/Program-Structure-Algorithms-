def dfs_with_pre_post(graph):
    visited = set()
    pre = {}
    post = {}
    clock = [1]

    def explore(v):
        visited.add(v)
        pre[v] = clock[0]
        clock[0]+=1
        for neighbor in graph[v]:
            if neighbor not in visited:
                explore(neighbor)

        post[v] = clock[0]
        clock[0]+=1

    for v in graph:
        if v not in visited:
            explore(v)

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