# def get_Smallest_Task_1(k, takeCosts):
#
#     n = len(takeCosts)
#
#     # Initialize DP table
#     # dp[i][j] represents whether it's possible to form sum j using a subsequence.
#
#     dp = [[-1] * k+1 for _ in range(n+1)]
#     dp[0][0]  = 0
#
#     # Variable to track the minimum subarray length
#     ans = float('inf')
#
#     # Loop each item
#     for i in range(1, n + 1):
#         cost = takeCosts[i]
#
#         # Loop over all sums for 0 to k
#         for j in range(k + 1):
#             dp[i][j] = dp[i-1][j]
#             if cost <= j and dp[i-1][j - cost] != -1:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j - cost])
#
#             if cost == j:
#                 dp[i][j] = max(dp[i][j], i - 1)
#
#         # If current subsequence is equal to k
#         if dp[i][k] != -1:
#             length = i - dp[i][k]
#             ans = min(length, ans)
#
#     return -1 if ans == float('inf') else ans
#
#
#
#

def solution(k, taskCosts):
    # The length of taskCosts
    n = len(taskCosts)

#Initialize the DP table
#dp[i][j] represents whether it's possible to form sum j using a sequence
    dp = [[-1] * k + 1 for _ in range(n + 1)]
    dp[0][0] = 0
    ans = float('inf')

    # Loop over the item from 1 to n
    for i in range(1, n + 1):
        cost = taskCosts[i - 1]
        #Loop over all sums from 0 to k
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if cost <= j and dp[i - 1][ j - cost] != -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j -cost])
            if cost == j:
                dp[i][j] = max(dp[i][j], i - 1)

        #If current subsequence is equal to k
        if dp[i][k] != -1:
            length = i - dp[i][k]
            ans = min(length, ans)

    return ans



