N = int(input())
arr = []

for i in range(N):
    arr.append(input().split())
length = len(arr)
result = []
for i in range(length):
    rank = 1
    for j in range(length):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    result.append(rank)

for i in result:
    print(i, end=' ')