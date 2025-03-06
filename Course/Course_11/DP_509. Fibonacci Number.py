# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
#


class Solution(object):
    def fib(self, n):
        #DP
        # if n <=1:
        #     return n
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[0] = 0
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        #
        # return dp[n]

        #Recursion
        if n ==0:
            return 0
        if n ==1:
            return 1
        return self.fib(n-1)+self.fib(n-2)

# Test case
sol = Solution()
print(sol.fib(5))  # Output: 5