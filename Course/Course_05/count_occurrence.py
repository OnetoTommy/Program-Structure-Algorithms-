# You are given a sorted array of integers A[1 : n] that may or may not contain duplicate values.
# You are also given a target integer k. You want to find out if there strictly more than one occurrence
# of k in A[1 : n] and the count of the occurrence.
from fontTools.merge.util import first


class Solution:
    def __init__(self, A):
        self.A = A

    def countOccurrence(self, k):
        n = len(self.A)
        first = self.first_index(0, n - 1, k)
        last = self.last_index(0, n - 1, k)

        # 如果未找到目标值 k，返回 0
        if first == -1 or last == -1:
            return 0

        return last - first + 1

    def first_index(self, l, r, k):

        while l <= r:
            mid = l + (r - l) // 2
            if self.A[mid] == k:
                if self.A[mid - 1] != k or mid == l:
                    return mid
                else:
                    r = mid - 1
            elif self.A[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    def last_index(self, l, r, k):
        while l <= r:
            mid = l + (r - l) // 2
            if self.A[mid] == k:
                if self.A[mid + 1] != k or mid == r:
                    return mid
                else:
                    l = mid + 1
            elif self.A[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
        return -1

A = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
k = 7
counter = Solution(A)
count = counter.countOccurrence(k)
print(count)