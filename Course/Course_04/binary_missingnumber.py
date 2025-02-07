# 给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。


class Solution:
    def __init__(self, arr):
        self.arr = arr
    def missingNumber(self):
        n = len(self.arr)
        totalSum = n * (n + 1) // 2
        actualSum = 0
        for i in range(n):
            actualSum += self.arr[i]

        return totalSum - actualSum

A = [0,1,2,4,5,6]
Num = Solution(A)
print(Num.missingNumber())
