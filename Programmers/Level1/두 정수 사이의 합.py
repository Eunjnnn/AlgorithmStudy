def solution(a, b):
    answer = 0
    if a == b:
        answer = a
    elif a > b:
        for i in range(b, a+1):
            answer += i
    else:
        for i in range(a, b+1):
            answer += i
    return answer

"""
def adder(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))

* 이렇게 간결하다니,, sum함수와 range함수 사용,,✨
"""