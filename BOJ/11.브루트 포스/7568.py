N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
# print(arr)

length = len(arr)
result = []
for i in range(length):
    rank = 1
    for j in range(length):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank, end=' ')
