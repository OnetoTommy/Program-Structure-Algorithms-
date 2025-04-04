
def solution(nums, i, memo = None):
    if memo == None:
        memo = {}
    if i in memo:
        return memo[i]

    if i == len(nums) - 1:
        return nums[i]
    sum = max(nums[i], solution(nums, i+1, memo) + nums[i])
    print(sum)
    memo[i] = sum
    return sum

def result(nums):
    return max(solution(nums,i) for i in range(len(nums)))



if __name__ == '__main__':
    num = [3,-4,2,-2,2,6,-5,4]
    print(result(num))