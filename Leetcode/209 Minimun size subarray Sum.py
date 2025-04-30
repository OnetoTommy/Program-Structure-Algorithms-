class Solution:
    def minSubArrayLen(self, num: list[int], target: int) -> int:
        # running time is O(n)
        # Space complexity is O(1)

        # Calculate the length of num
        n = len(num)
        # Define the length of minimum size
        ans = n + 1
        # Define the left pointer
        left = 0
        # Define the sum of s
        s = 0
        for i, x in enumerate(num):
            s += x
            while s - num[left] >= target:
                s -= num[left]
                left += 1
            if s >= target:
                ans = min(ans, i - left + 1)
        return ans if ans < n+1 else 0

if __name__ == '__main__':
    s = Solution()
    num = [2,3,1,2,4,3]
    target = 7
    print(s.minSubArrayLen(num,target))

