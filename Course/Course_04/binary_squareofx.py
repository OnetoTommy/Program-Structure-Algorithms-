class Solution:

    def square_of_x(self, x):
        l = 0
        r = x
        nums = -1
        while(l < r):
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid
            else:
                l = mid + 1
                nums = mid

        return nums

x = Solution()
num = x.square_of_x(17)
print(num)