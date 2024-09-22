def solution(nums):
    numSet = set(nums)
    answer = min(len(nums)//2, len(numSet))
    return answer