def rotation(A, k):
    array = []
    if k <= 0:
         return A
    if k > 0:
        length = len(A)
        array.append(A[length-1])
        for j in range(length-2):
            array.append(A[j])
        k = k-1
        return rotation(array,k)

    return array

def find_rotation_count(arr, low, high):

    # If the array is already sorted
    if arr[low] <= arr[high]:
        return low  # The array is not rotated

    mid = low + (high - low) // 2

    # Check if mid+1 is the smallest
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid + 1

    # Check if mid is the smallest
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid

    # Recur into the unsorted half
    if arr[mid] >= arr[low]:
        return find_rotation_count(arr, mid + 1, high)
    else:
        return find_rotation_count(arr, low, mid - 1)

# Driver Code
A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
k = 3

array = rotation(A, k)
print(array)

result = find_rotation_count(array, 0, len(array) - 1)
if result != -1:
 print(result)
else:
 print(result)
