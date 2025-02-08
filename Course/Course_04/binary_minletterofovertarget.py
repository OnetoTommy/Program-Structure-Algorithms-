# 744 给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。
# https://leetcode.cn/problems/find-smallest-letter-greater-than-target/description/?envType=problem-list-v2&envId=binary-search
# 返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。
class solution:
    def minletteroftarget(self, letters, target):
        r = len(letters) - 1
        l = 0

        while l <= r:
            mid = (l + r) // 2
            if letters[mid] > target:
                if letters[mid - 1] <= target:
                    return letters[mid]
                else:
                    r = mid - 1
            else:
                l = mid + 1

        return letters[0]

letters = ["c", "f", "j"]
target = "a"
string = solution()
print(string.minletteroftarget(letters, target))
