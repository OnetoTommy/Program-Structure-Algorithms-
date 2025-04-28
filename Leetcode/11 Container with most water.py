class Solution:
    def maxArea(self, height):
        # Running Time is O(n)
        # Space complexity is O(1)
        n = len(height)
        left = 0
        right = n - 1
        ans = 0
        while left < right:
            min_height = min(height[left], height[right])
            ans = max(ans, min_height * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))