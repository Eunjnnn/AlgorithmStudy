def solution(lottos, win_nums):
    answer = [0] * 2
    cnt = 0
    zero = 0
    rank = [6,6,5,4,3,2,1]
    
    for i in lottos:
        if i == 0: zero = zero + 1
        for j in win_nums:
            if i == j: cnt = cnt + 1
    
    # print(cnt, zero)
    answer[0] = rank[cnt + zero]
    answer[1] = rank[cnt]
    
    return answer