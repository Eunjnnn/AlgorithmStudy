#############################
##         다시 풀어보기      ##
#############################

def solution(s):
    answer = 10000
    for i in range(1, len(s)//2 + 2):
        prev = ''
        count = 1
        now = s[:i]
        
        for j in range(i, len(s) + i, i):
            if now == s[j:j+i]:
                count += 1
            else:
                if count == 1:
                    prev += now
                else:
                    prev += str(count) + now
                now = s[j:j+i]
                count = 1
        # print(prev)
        answer = min(answer, len(prev))
        
    return answer
