def solution(record):
    answer = []
    states = []     # "Enter", "Leave", "Change"
    user_dict = {}
    
    for rec in record:
        now = rec.split()
        state, userid = now[0], now[1]
        # print(state, userid)
        
        if state == 'Enter' or state == 'Change':
            name = now[2]
            user_dict[userid] = name
        states.append([state, userid])
    
    # print(user_dict)
    
    for state_info in states:
        state, userid = state_info[0], state_info[1]
        # print(user_dict[userid])
        if state_info[0] == 'Enter':
            answer.append(f'{user_dict[userid]}님이 들어왔습니다.')
        elif state_info[0] == 'Leave':
            answer.append(f'{user_dict[userid]}님이 나갔습니다.')
    
    return answer