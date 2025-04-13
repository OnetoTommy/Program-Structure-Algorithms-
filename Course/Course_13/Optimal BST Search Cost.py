import math

def optimal_bst(p, q, n):
    # 初始化 e, w, root 三个表格
    e = [[0] * (n + 2) for _ in range(n + 2)]  # e[i][j]: 最小期望代价
    w = [[0] * (n + 2) for _ in range(n + 2)]  # w[i][j]: 权重和
    root = [[0] * (n + 1) for _ in range(n + 1)]  # root[i][j]: 最优根的位置

    # 初始化 base case: e[i][i-1] = 0, w[i][i-1] = q[i-1]
    for i in range(1, n + 2):
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]

    # 开始填表
    for l in range(1, n + 1):  # l 是子树长度
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = math.inf
            w[i][j] = w[i][j - 1] + p[j - 1] + q[j]

            for r in range(i, j + 1):  # 枚举所有可能的根
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r

    return e, root

p = [0.15, 0.10, 0.05, 0.10, 0.20]
q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
n = 5

e, root = optimal_bst(p, q, n)
print("Minimum expected search cost:", e[1][n])
print("Root table:")
for row in root[:]:
    print(row[:])
