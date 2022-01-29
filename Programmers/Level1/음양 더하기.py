def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == 1:   answer += abs(absolutes[i])
        else:   answer -= abs(absolutes[i])
    return answer


## zip 함수 사용!!
### WOW,,,,
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))