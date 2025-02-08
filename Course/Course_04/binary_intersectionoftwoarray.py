# 给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
# 应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
# 350--https://leetcode.cn/problems/intersection-of-two-arrays-ii/description/?envType=problem-list-v2&envId=binary-search


class Solution:
    def intersect(self, nums1, nums2):
        """
               :type nums1: List[int]
               :type nums2: List[int]
               :rtype: List[int]
               """

        hashlist = [0] *1000
        temp = [0] * 1000
        result = []
        for i in nums1:
            hashlist[i] += 1

        for i in nums2:
            if hashlist[i] > 0:
                hashlist[i] -= 1
                temp[i] += 1

        for i in range(len(temp)):
            if temp[i] > 0:
                count = temp[i]
                while count > 0:
                    result.append(i)
                    count -= 1
        return result

nums1 = [1,2,2,1]
nums2 = [2,2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

a = Solution()
print(a.intersect(nums1, nums2))