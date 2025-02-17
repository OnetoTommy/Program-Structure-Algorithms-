def heapify(arr, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i 
    if left < n and arr[left] > arr[largest]:
        largest = left 
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        arr = heapify(arr, n, largest)
    

def buildMaxHeap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    return arr

def heapsort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    arr = buildMaxHeap(arr)
    print("Array after maxheap: {}".format(arr))
    for i in range(n-1, 0, -1):
        print("Swaping index: %d with %d"%(i, 0))
        arr[i], arr[0] = arr[0], arr[i]
        #print("Before heapify", arr)
        heapify(arr, i, 0)
        #print("After heapify: ",arr)
    return arr


# Example usage:
arr = [5, 3, 2, 1, 4]
heapsort(arr)
print("Final sorted: ", arr)