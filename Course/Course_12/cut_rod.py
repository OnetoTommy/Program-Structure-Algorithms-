#求一定长度铁棒的切割最大价值，整体思路先求最小的长度最大价值，逐步递归
# p and l

# def solution(p, l):
#
#     dp = [0] * (l+1)
#     for i in range(l+1):
#         for j in range(i+1):
#             dp[i] = max(dp[i], p[j] + dp[i-j])
#     return dp[l]





if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
    debug = 2
    print(solution(p, len(p)-1))


