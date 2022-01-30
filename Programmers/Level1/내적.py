def solution(a, b):
    answer = 0
    
    for x, y in zip(a, b):
        answer += x * y
    
    return answer

# 줄이면  ===> sum([x*y for x, y in zip(a,b)])