class Solution:
    def threeSum(self, nums:list[int]) -> list[list[int]]:
        # Running time is O(nlogn)
        nums.sort()
        n = len(nums)
        ans = []

        # Running time is O(n^2)
        # Space Complexity is O(1)
        for i in range(n-2):
            x = nums[i]

            # Avoid the duplicate result
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Optimization code for running time
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[n-1] + nums[n-2] < 0:
                continue

            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[i], nums[k]])
                    # Avoid the duplicate result
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))