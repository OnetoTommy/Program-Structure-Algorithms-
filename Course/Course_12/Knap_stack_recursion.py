def knapsack_recursive(values, weights, W, n):
    # If the weight of the current item is more than the remaining capacity, exclude it
    if weights[n - 1] > W:
        return knapsack_recursive(values, weights, W, n - 1)
    else:
        # Otherwise, consider both possibilities: including or excluding the item
        include_item = values[n - 1] + knapsack_recursive(values, weights, W - weights[n - 1], n - 1)
        exclude_item = knapsack_recursive(values, weights, W, n - 1)

        # Return the maximum of both options
        return max(include_item, exclude_item)



# Example usage:
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]  # Weights of the items
W = 50  # Maximum weight capacity of the knapsack
n = len(values)  # Number of items

# Call the recursive knapsack function and print the result
result = result(values, weights, W)
print(f"The maximum value that can be obtained is {result}")
