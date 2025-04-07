
# def solution(nums, i, memo = None):
#     if memo == None:
#         memo = {}
#     if i in memo:
#         return memo[i]
#
#     if i == len(nums) - 1:
#         return nums[i]
#     sum = max(nums[i], solution(nums, i+1, memo) + nums[i])
#     print(sum)
#     memo[i] = sum
#     return sum
#
# def result(nums):
#     return max(solution(nums,i) for i in range(len(nums)))


# Bottom to Top
# def solution(nums):
#     n = len(nums)
#     dp = [0] * n
#     for i in range(n):
#         dp[i] = nums[i]
#     for i in range(n):
#         sum = nums[i]
#         for j in range(i+1, n):
#             sum += nums[j]
#             dp[i] = max(dp[i], sum)
#     print(dp)
#     return max(dp)

def solution(nums, i):
    sum = float('-inf')
    s = nums[i]
    for j in range(i+1, len(nums)):
        s += nums[j]
        sum = max(sum, s)
    return sum

def result(nums):
    dp = [float('-inf')] * len(nums)
    max_num = float('-inf')
    for i in range(len(nums)):
        max_num = max(max_num, solution(nums, i))
        dp[i] = max_num
    return max(dp)

if __name__ == '__main__':
    num = [3,-4,2,-1,2,6,-5,4]
    print(result(num))