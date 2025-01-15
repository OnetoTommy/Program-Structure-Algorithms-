#Ω(1) - Constant Time (Linear Search - Best Case):

def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            print(f"Number of steps taken: {steps}")
            return i
    print(f"Number of steps taken: {steps}")
    return -1  # Element not found

# Example usage
arr = [5, 2, 4, 6, 1, 3]
target = 5
index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index: {index}")
else:
    print(f"Element {target} not found in the array.")
print("-------------")

#Ω(n) - Linear Time (Bubble Sort - Best Case):

def bubble_sort(arr):
    steps = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            steps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    print(f"Number of steps taken: {steps}")

# Example usage
arr = [1, 2, 3, 5, 6]
print("Before Sorting:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
print("-------------")

#Ω(n²) - Quadratic Time (Redundant Sort):
def selection_sort(arr):
    steps = 0
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted array
        min_idx = i
        for j in range(i+1, n):
            steps += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    print(f"Number of steps taken: {steps}")
    return arr

# Example usage
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array:", arr)
print("-------------")

#Ω(n log n) - Linearithmic Time (QuickSort - Best Case):
def quick_sort(arr, steps=[0]):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for x in arr[1:]:
            steps[0] += 1
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)
        return quick_sort(less, steps) + [pivot] + quick_sort(greater, steps)

# Example usage
arr = [3, 2, 1, 5, 4]
steps = [0]
sorted_arr = quick_sort(arr, steps)
print("Sorted array:", sorted_arr)
print(f"Number of steps taken: {steps[0]}")
print("-------------")