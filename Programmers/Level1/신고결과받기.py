def solution(id_list, report, k):
    id_index = {}   # id를 숫자로 변환
    list_len = len(id_list)
    rep_list = [set() for _ in range(list_len)] #rep_list[i]:i 를 신고한 사람의 집합
    answer = [0] * list_len
    
    for i in range(list_len):
        id_index[id_list[i]] = i
    
    for case in report:
        user1, user2 = case.split()
        rep_list[id_index[user2]].add(id_index[user1])
    
    for i in range(list_len):
        if len(rep_list[i]) < k : continue
        for x in rep_list[i]: answer[x] += 1
    
    return answer