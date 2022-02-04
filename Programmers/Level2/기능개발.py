def solution(progresses, speeds):
    answer = []
    days = []
    
    for prog, speed in zip(progresses, speeds):
        day = 0
        while prog < 100 :
            day += 1
            prog += speed
        days.append(day)
    
    # print(days)
    
    # front를 0으로 초기화 해놓고 배열을 돌아갈때 index와 비교해서 그 차이를 answer에 넣는다.
    # front에 최신 index 값을 저장해놓았기 때문에 for 문이 끝나면 마지막 차이를 구할 수 있다.
    front = 0
    for idx in range(len(days)):
        if days[idx] > days[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(days) - front)
        
    return answer


## Queue FIFO 활용
""" def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer """