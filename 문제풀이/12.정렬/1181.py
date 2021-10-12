N = int(input())
lst = []

for i in range(N):
    lst.append(input())
set_lst = set(lst)	## set으로 변환해서 중복값을 제거
lst = list(set_lst)	## 다시 list로 변환
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)



'''
for i in range(N):
    str = input()
    str_len = len(str)
    arr.append([str_len, str])

arr.sort()      # sort는 문자도 정렬해
for i in range(N):
    if arr[i][1] == arr[i-1][1]:
        continue
    else: print(arr[i][1])
'''