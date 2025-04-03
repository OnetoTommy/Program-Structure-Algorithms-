def knapsack(values, weights, W):
    n = len(values)
    K = [0] * (W + 1)
    s = [-1] * (W + 1)
    for w in range(1, W + 1):
        for i in range(n):
            if weights[i] <= w:
                K[w] = max(K[w], K[w - weights[i]] + values[i])
                s[w] = values[i]
    return K, s



# Example usage:
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]  # Weights of the items
W = 50  # Maximum weight capacity of the knapsack

# Call the knapsack function and print the result
k,s = knapsack(values, weights, W)
for i in range(W+1):
    print("%d,%d"%(k[i], s[i]))


