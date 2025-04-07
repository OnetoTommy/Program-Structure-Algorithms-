# def getSmallestTaskSubarray(k, taskCosts):
#     n = len(taskCosts)
#     dp = [[-1] * (k + 1) for _ in range(n + 1)]
#     dp[0][0] = 0
#     ans = float('inf')
#     for i in range(1, n + 1):
#         cost = taskCosts[i - 1]
#         for s in range(k + 1):
#             dp[i][s] = dp[i - 1][s]
#             if s >= cost and dp[i - 1][s - cost] != -1:
#                 dp[i][s] = max(dp[i][s], dp[i - 1][s - cost])
#             if cost == s:
#                 dp[i][s] = max(dp[i][s], i - 1)
#         if dp[i][k] != -1:
#             length = i - dp[i][k]
#             ans = min(ans, length)
#     return -1 if ans == float('inf') else ans


def getSmallestTaskSubarray(k, taskCosts):
    n = len(taskCosts)

    # Initialize DP table:
    # dp[i][s] represents whether it's possible to form sum s using a subsequence
    # from the subarray taskCosts[dp[i][s] : i]
    # If possible, store the starting index of that subarray; otherwise, -1
    dp = [[-1] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base case: sum 0 is possible with empty subsequence, starting at index 0

    ans = float('inf')  # Variable to track the minimum subarray length

    # Loop over each task position (1-based for easier DP indexing)
    for i in range(1, n + 1):
        cost = taskCosts[i - 1]  # Current task's cost

        # Loop over all target sums from 0 to k
        for s in range(k + 1):
            # Case 1: don't take current task; inherit value from previous row
            dp[i][s] = dp[i - 1][s]

            # Case 2: take current task as part of a subsequence
            if s >= cost and dp[i - 1][s - cost] != -1:
                # If previous sum (s - cost) was achievable, update dp[i][s]
                dp[i][s] = max(dp[i][s], dp[i - 1][s - cost])

            # Case 3: current task alone makes up the target sum s
            if cost == s:
                dp[i][s] = max(dp[i][s], i - 1)

        # If current subarray (ending at i) has a subsequence summing to k
        if dp[i][k] != -1:
            length = i - dp[i][k]  # Calculate subarray length
            ans = min(ans, length)  # Update the minimum length

    # Return the result: -1 if not found, otherwise the minimum length
    return -1 if ans == float('inf') else ans
