def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]-1
        j = c[1]
        k = c[2]
        arr = sorted(array[i: j])
        answer.append(arr[k-1])
    return answer

# WOW,,
"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""