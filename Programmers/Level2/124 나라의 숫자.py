def solution(n):
    answer = ''
    
    num = ['1', '2', '4']
    rest = 0
    # rest = n % 3
    
    while n > 0:
        n -= 1
        rest = n % 3
        if rest == 0:
            answer = num[0] + answer
        elif rest == 1:
            answer = num[1] + answer
        else:
            answer = num[2] + answer
        # answer = num[rest] + answer
        n = n // 3
    
    return answer