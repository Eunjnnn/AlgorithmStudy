def solution(n):
    answer = 0
    three_n = ''
    while n:
        three_n += str(n % 3)
        # print(three_n)
        n = n // 3
    
    return int(three_n, 3)