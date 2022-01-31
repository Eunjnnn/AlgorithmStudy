from itertools import combinations

def primenumber(num):
    if num == 1:
        return True
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
                

def solution(nums):
    answer = 0
    li = list(combinations(nums, 3))
    
    for i in li:
        if primenumber(sum(i)):
            answer += 1

    return answer