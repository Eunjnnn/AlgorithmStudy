def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        s = 0
        measure = []
        for i in range(1, num+1):
            if num % i == 0:
                measure.append(i)
        print(measure)
        if len(measure) % 2 == 0:
            answer += num
        else:
            answer -= num
    return answer

# wow,,
"""
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
"""