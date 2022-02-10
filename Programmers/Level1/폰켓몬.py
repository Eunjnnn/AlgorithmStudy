def solution(nums):
    answer = 0
    type = {}
    for n in nums:
        type[n] = 0
    for n in nums:
        type[n] += 1
    # print(type)
    if len(type.keys()) > (len(nums) //2):
        return (len(nums) //2)
    else:   return len(type.keys())

# WOW,,,
"""
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
"""