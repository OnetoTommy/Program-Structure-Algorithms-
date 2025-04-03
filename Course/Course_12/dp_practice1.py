def result(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]

    for i in range(1, n):
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
        max_sum = max(max_sum, dp[i])

    return max_sum


if __name__ == '__main__':
    num = [3,-4,2,-2,2,6,-5,4]
    print(result(num))