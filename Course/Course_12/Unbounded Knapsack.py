def unbounded_knapsack(weights, values, capacity):
    n = len(weights)
    # DP array, where dp[w] = max value achievable with weight w
    dp = [0] * (capacity + 1)

    # Build up dp from weight 1 to W
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

weights = [1, 2, 3]
values = [7, 3, 20]
capacity = 58
print(unbounded_knapsack(weights, values, capacity))  # 输出最大总价值
