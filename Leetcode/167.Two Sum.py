class Solution:
    def twoSum(self, nums:[int], target: int) -> [int]:
        # Running time O(n)
        # Space Complexity O(1)
        # Define the left and right of pointer
        left = 0
        right = len(nums) - 1
        # Loop for sum
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                break
            elif s < target:
                left += 1
            else:
                right -= 1
        return [left + 1, right + 1]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))
