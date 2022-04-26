def solution(n, arr1, arr2):
    answer = []
    for i in range(0, n):
        row = ""
        arr1_d = format(arr1[i], 'b').zfill(n)
        arr2_d = format(arr2[i], 'b').zfill(n)
        for j in range(0, n):
            if arr1_d[j] == '1' or arr2_d[j] == '1':
                row += "#"
            else:
                row += " "
        answer.append(row)
    return answer