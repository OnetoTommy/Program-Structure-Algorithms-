# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.

class Solution(object):
    def minCostClimbingStairs(self, cost):

        n = len(cost)
        if n <=1:
            return 0
        dp = [0] * (n + 1)
        dp[1] = 0
        dp[0] = 0
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], cost[i - 2]+dp[i - 2])

        return dp[n]
sol = Solution()
c =[10, 15, 20]
print(sol.minCostClimbingStairs(c))