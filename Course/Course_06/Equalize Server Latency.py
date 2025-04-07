# def dfs(node_index, latency, total_additional_latency):
#     left_child_index = 2 * node_index + 1
#     right_child_index = 2 * node_index + 2
#
#     left_delay = right_delay = 0
#
#     if left_child_index < len(latency):
#         left_delay = latency[left_child_index] + dfs(left_child_index, latency, total_additional_latency)
#     if right_child_index < len(latency):
#         right_delay = latency[right_child_index] + dfs(right_child_index, latency, total_additional_latency)
#
#     total_additional_latency[0] += abs(left_delay - right_delay)
#
#     return max(left_delay, right_delay)

# def minAdditionalLatency(n, latency):
#     lat = latency[:]
#     def dfs(i: int) -> (int, int):
#         if i >= (n - 1) // 2:
#             return 0, 0
#         l, r = 2 * i + 1, 2 * i + 2
#         l_cost, l_extra = dfs(l)
#         r_cost, r_extra = dfs(r)
#         l_total = l_cost + lat[l - 1]
#         r_total = r_cost + lat[r - 1]
#         max_path = max(l_total, r_total)
#         return max_path, l_extra + r_extra + (max_path - l_total) + (max_path - r_total)
#     return dfs(0)[1]


# def dfs(i: int, n: int, latency:list) -> (int, int):
#     lat = latency[:]
#     if i >= (n - 1) // 2:
#         return(0, 0)
#     l = 2 * i + 1
#     r = 2 * i + 2
#     l_cost, l_extra = dfs(l, n, lat)
#     r_cost, r_extra = dfs(r, n, lat)
#     l_total = l_cost + lat[l - 1]
#     r_total = r_cost + lat[r - 1]
#     max_side = max(l_total, r_total)
#     return max_side, l_extra + r_extra + (max_side - l_total) + (max_side - r_total)
#
# def minAdditionalLatency(n: int, latency:list) -> int:
#     return dfs(0, n, latency)[1]




# def minAdditionalLatency(latency):
#     total_additional_latency = [0]
#     dfs(0, latency, total_additional_latency)
#     return total_additional_latency[0]


def dfs(i:int, n: int, latency:list) -> (int, int):
    lat = latency[:]

    # Base case: if the current node is a leaf node, return (cost, extra_latency) = (0, 0)
    if i >= (n - 1) // 2:
        return(0, 0)

    # Compute indices of left and right child nodes in a complete binary tree
    l_node = 2 * i + 1
    r_node = 2 * i + 2

    # Recursively calculate cost and extra latency for both children
    l_cost, l_extra = dfs(l_node, n, lat)
    r_cost, r_extra = dfs(r_node, n, lat)

    # Total cost to reach the leaves through left and right paths
    l_total_cost = l_cost + lat[l_node - 1]
    r_total_cost = r_cost + lat[r_node - 1]

    # Find the longer path to balance the shorter one
    max_val = max(l_total_cost, r_total_cost)

    # Return:
    # 1. max_val: the max cost from this node to leaf
    # 2. extra latency needed to balance both paths
    return max_val, l_extra + r_extra + (max_val - l_total_cost) + (max_val - r_total_cost)

def minAdditionalLatency(n: int, latency: list):

    return dfs(0, n, latency)[1]










# print(minAdditionalLatency(3,[10, 5]))  # 输出: 5
print(minAdditionalLatency(7, [5, 5, 5, 5, 5, 5]))  # 完全平衡，输出: 0
# print(minAdditionalLatency(7,[1, 2, 3, 4, 5, 6]))  # 输出: ?
