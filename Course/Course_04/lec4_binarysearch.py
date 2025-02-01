def binarySearch(A, lo, hi, x):

    if lo <= hi:

        ## integer division
        mid = lo + (hi - lo) // 2

        #print("low = %d ; high = %d ; mid = %d, elem = %d"%(lo, hi, mid, A[mid]))

        # Check if x is present at mid
        if A[mid] == x:
            #print("Element found at index: %d"%(mid))
            return mid

        # If x is greater, ignore left half
        elif A[mid] < x:
            lo = mid + 1
            return binarySearch(A, lo, hi, x)

        # If x is smaller, ignore right half
        else:
            hi = mid - 1
            return binarySearch(A, lo, hi, x)

    else:
        # If we reach here, then the element was not present
        #print("Element not found")
        return -1


# Driver Code
# if __name__ == '__main__':
A = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
x = 5

# Function call
lo = 0
hi = len(A) - 1
result = binarySearch(A, lo, hi, x)
if result != -1:
    print("Element %d is present at index: %d"%(x, result))
else:
    print("Element %d is not present in array"%(x))