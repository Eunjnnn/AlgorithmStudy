def solution(board, moves):
    length = len(board)
    answer = []
    basket = []
    
    for x in moves:
        x = x-1
        for y in range(0, length):
            now = board[y][x]
            if now == 0:
                continue
            else:
                #### 만약 같은 인형이 2개 이상으로 중복된다면? 
                #### 같은 인형이 엄~청 많이 나올 수도 있다,,
                
                # if not len(basket):
                #     basket.append(now)
                # elif basket[-1] == now:
                #     answer += 2
                #     basket.remove(basket[-1])
                # else:
                #     basket.append(now)
                
                basket.append(now)
                board[y][x] = 0
                if basket[-1:] == basket[-2:-1]:
                    answer += basket[-1:]
                    basket = basket[:-2]
                break
    
    return len(answer)*2