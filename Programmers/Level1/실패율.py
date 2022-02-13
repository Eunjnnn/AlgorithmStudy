def solution(N, stages):
    status = {}
    people = len(stages)
    
    for stage in range(1, N+1):
        if people == 0:
            status[stage] = 0
            continue
        count = stages.count(stage)
        status[stage] = count / people
        people -= count

    print(status)
    answer = sorted(status, key=lambda x: status[x], reverse = True)
    # status는 dictionary이므로 sorted에 result를 그냥 넘기면 result의 keys가 들어갑니다.
    # keys는 생략이 가능합니다. 거기에 lambda는 기준을 status[x]: 즉 value로 정렬한다는 뜻
    return answer