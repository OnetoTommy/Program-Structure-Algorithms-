def lcs_bt(x, y):
    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1,-1, -1):
            if x[i] == y[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    return dp[0][0]

if __name__ == '__main__':
    x = 'character'
    y = x[::-1]
    print(lcs_bt(x, y))