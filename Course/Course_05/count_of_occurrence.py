# You are given a sorted array of integers A[1 : n] that may or may not contain duplicate values.
# You are also given a target integer k. You want to find out if there strictly more than one occurrence
# of k in A[1 : n] and the count of the occurrence.
from fontTools.merge.util import first


class Count_Occurrence:
    def __init__(self, A):
        self.A = A

    def first_index(self, l, h, k):
        if l > h:
            return False

        mid = (l + h) // 2
        if A[mid] == k:
            if mid == l or A[mid - 1] != k:
                return mid
            else:
                return self.first_index(l, mid-1, k)

        elif A[mid] > k:
            return self.first_index(l, mid-1, k)
        else:
            return self.first_index(mid+1, h, k)

    def last_index(self,  l, h, k):
        if l > h:
            return False

        mid = (l + h) // 2
        if A[mid] == k:
            if mid == h or A[mid + 1] != k:
                return mid
            else:
                return self.last_index(mid+1, h, k)

        elif A[mid] > k:
            return self.last_index(l, mid - 1, k)
        else:
            return self.last_index(mid + 1, h, k)

    def count_occurrence(self, k):
        n = len(self.A)
        first_index = self.first_index(0, n-1, k)
        if first_index == False:
            return False
        last_index = self.last_index(0, n-1, k)
        count = last_index - first_index + 1

        return count


A = [2,5,5,5,6,6,8,9,9,9]
k=7
counter = Count_Occurrence(A)
count = counter.count_occurrence(k)
print(count)