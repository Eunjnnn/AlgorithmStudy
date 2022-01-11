def solution(n):
    N = [int(i) for i in str(n)]
    return sum(N)


N = int(input())
const = [0 for i in range(N)]
min_const = 0

for i in range(N):
    const[i] = solution(i) + i
    if const[i] == N:
        min_const = i
        break
    else:
        min_const = 0

print(min_const)