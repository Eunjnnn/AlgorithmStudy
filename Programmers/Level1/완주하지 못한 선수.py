def solution(participant, completion):
    answer = ''
    part_dict = {}
    temp = 0
    
    for i in participant:
        # participant 요소의 해시값을 part_dict의 key로 넣어주고,
        # participant 요소를 value로 넣어준다.
        part_dict[hash(i)] = i
        
        temp += hash(i)
    
    for com in completion:
        # completion 요소들의 해시값을 temp 에서 다 빼준다.
        # 전제에 완주하지 못한 사람은 1명이라고 했으니, 다 빼주고 나면 1명의 해시값만 남는다.
        temp -= hash(com)
        
    answer = part_dict[temp]
    
    return answer