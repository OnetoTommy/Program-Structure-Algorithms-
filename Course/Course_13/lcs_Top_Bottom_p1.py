def lcs_tb(x:str, y:str) -> int:
    m = len(x)
    n = len(y)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

if __name__ == '__main__':
    x = 'character'
    y = x[::-1]
    print(lcs_tb(x, y))