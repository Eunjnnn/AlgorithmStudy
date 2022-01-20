def solution(new_id):
    answer = ''
    # 1 단계 
    new_id = new_id.lower()
    
    # 2 단계
    for str in new_id:
        if str.isalpha() or str.isdigit() or str in ["-", "_", "."]:
            answer += str
    
    # 3 단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4 단계
    answer = answer.lstrip(".")
    answer = answer.rstrip(".")
    
    # 5 단계
    if not answer:
        answer = "a"
    
    # 6 단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[len(answer)-1] == '.':
        answer = answer.rstrip(".")
    
    # 7 단계
    while len(answer) <= 2:
        answer += answer[len(answer)-1]
    
    print(answer)

    return answer

## answer[len(answer)-1] ==> answer[-1]