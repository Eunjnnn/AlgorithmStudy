N = int(input())

arr = []
for i in range(N):
    age, name = map(str, input().split())
    age_num = int(age)
    arr.append([age_num, name])

arr.sort(key=lambda x:x[0])
for i in range(N):
    print(arr[i][0], arr[i][1])