def getSmallestTaskSubarray(k, taskCosts):
    from collections import defaultdict
    n = len(taskCosts)

    # dp[s] = 最短长度（组成 sum=s 的子序列）
    dp = {0: 0}

    for cost in taskCosts:
        new_dp = dp.copy()
        for s in dp:
            total = s + cost
            if total > k:
                continue
            if total not in new_dp or new_dp[total] > dp[s] + 1:
                new_dp[total] = dp[s] + 1
        dp = new_dp

    return dp[k] if k in dp else -1


# 示例测试
print(getSmallestTaskSubarray(14, [3, 2, 3, 12]))  # 输出: 2 (例如 [2,12])
