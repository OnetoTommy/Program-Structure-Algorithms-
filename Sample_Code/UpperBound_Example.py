# O(1) - Constant Time:
print("Example: Accessing an element in an array by its index.")
print("O(1)")
def access_element(arr, index):
    steps = 1  # Only one step is required to access an element
    print(f"Number of steps: {steps}")
    return arr[index]

# Example usage
arr = [10, 20, 30, 40, 50]
print("Result:", access_element(arr, 3))  # Accessing the 4th element
print("----")


# O(N) - Linear Time:
print("Example: Linear Search in an unsorted array.")
print("O(n)")
def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            print(f"Number of steps: {steps}")
            return i
    print(f"Number of steps: {steps}")
    return -1

# Example usage
arr = [5, 3, 8, 6, 7]
print("Target found at index:", linear_search(arr, 6))  # Searching for the number 6
print("----")


# O(n²) - Quadratic Time
print("Example: Bubble Sort algorithm.")
print("O(n²)")
def bubble_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(f"Number of steps: {steps}")
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array:", arr)
print("----")

#------------------------------------
print("Example: Recursive Fibonacci sequence.")
print("O(2^n)")

def fibonacci(n):
    if n <= 1:
        return (n, 1)  # Return the Fibonacci number and the count of 1 step
    else:
        fib_n_1, steps_n_1 = fibonacci(n-1)  # Recursive call for (n-1)th Fibonacci number
        fib_n_2, steps_n_2 = fibonacci(n-2)  # Recursive call for (n-2)th Fibonacci number
        return (fib_n_1 + fib_n_2, steps_n_1 + steps_n_2 + 1)  # Sum the results and steps, adding 1 for the current call

# Example usage
result, steps = fibonacci(6)  # 6th number in Fibonacci sequence
print("Fibonacci result:", result)
print("Number of steps taken:", steps)
print("----")


# fibonacci(6)
# ├── fibonacci(5)
# │   ├── fibonacci(4)
# │   │   ├── fibonacci(3)
# │   │   │   ├── fibonacci(2)
# │   │   │   │   ├── fibonacci(1)
# │   │   │   │   └── fibonacci(0)
# │   │   │   └── fibonacci(1)
# │   │   ├── fibonacci(2)
# │   │   │   ├── fibonacci(1)
# │   │   │   └── fibonacci(0)
# │   ├── fibonacci(3)
# │   │   ├── fibonacci(2)
# │   │   │   ├── fibonacci(1)
# │   │   │   └── fibonacci(0)
# │   │   └── fibonacci(1)
# └── fibonacci(4)
#     ├── fibonacci(3)
#     │   ├── fibonacci(2)
#     │   │   ├── fibonacci(1)
#     │   │   └── fibonacci(0)
#     │   └── fibonacci(1)
#     └── fibonacci(2)
#         ├── fibonacci(1)
#         └── fibonacci(0)

# For fibonacci(6), we calculated 25 steps, which is less than 2^6 (which equals 64). 
# The number of steps doesn't exactly match 2^n due to the base cases (where n is 0 or 1) that don't result in two further calls. 
# However, as n increases, the impact of these base cases becomes negligible, 
# and the growth rate of the number of calls closely approximates 2^n, justifying the Big O notation of O(2^n).

#--------------------------------
#O(log n) - Logarithmic Time:
print("Example: Binary Search algorithm")
print("O(log n)")
def binary_search(arr, low, high, target, steps=0):
    steps += 1
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            print(f"Number of steps: {steps}")
            return mid
        elif arr[mid] > target:
            return binary_search(arr, low, mid - 1, target, steps)
        else:
            return binary_search(arr, mid + 1, high, target, steps)
    else:
        print(f"Number of steps: {steps}")
        return -1

# Example usage
arr = [2, 3, 4, 10, 40]
target = 10
result = binary_search(arr, 0, len(arr)-1, target)
print("Element found at index:", result)
print("----")

# Initial Array: [2, 3, 4, 10, 40], Target = 10

# Step 1:
# - Range: [2, 3, 4, 10, 40] (Indices 0 to 4)
# - Mid Index: 2 (Value at mid: 4)
# - Since 4 < 10, discard left half (including mid). New Range: [10, 40]

# Step 2:
# - Range: [10, 40] (Indices 3 to 4)
# - Mid Index: 3 (Value at mid: 10)
# - 10 is the target. Search ends.
