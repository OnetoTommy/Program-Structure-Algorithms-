class Solution:
    def trap(self, height: list[int]) -> int:
        # Running time is O(n)
        # Space Complexity is O(n)
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i-1], height[i])
        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            suf_max[i] = max(suf_max[i+1], height[i])
        ans = 0
        for i in range(n):
            min_h = min(suf_max[i], pre_max[i])
            ans += min_h - height[i]
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1,7]))
