# calculate the biggest consistency numbers

def solution(nums, i, memo = None):
    if memo is None:
        memo = {}
    if i in memo:
        return memo[i]
    if i == len(nums) - 1:
        return 1
    n = len(nums)
    k = 1
    for j in range(i+1, n):
        if nums[j] > nums[i]:
            k = max(k, solution(nums, j, memo)+1)
    memo[i] = k
    return k

def result(num):
    return max(solution(num, i) for i in range(len(num)))


if __name__ == '__main__':
    # num = [3,-4,2,-2,2,6,-5,4]
    num = [1, 4, 2, 3, 5]
    print(result(num))