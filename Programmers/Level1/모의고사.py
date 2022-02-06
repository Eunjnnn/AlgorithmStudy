def solution(answers):
    answer = []
    counts = []
    student = {1 : [1, 2, 3, 4, 5] * 2000, 
               2 : [2, 1, 2, 3, 2, 4, 2, 5] * 2000,
               3 : [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000}
    
    for key, value in student.items():
        i = 0
        count = 0
        for v in value:
            if i < len(answers) and v == answers[i]:
                count += 1
            i += 1
        counts.append(count)
        
    m = max(counts)
    for i in range(len(counts)):
        if counts[i] == m:
            answer.append(i+1)
    
    return answer