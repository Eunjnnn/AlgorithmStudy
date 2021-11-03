N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
ans = int(1e9)

def dfs(index, count):
    global ans
    if count == N//2:
        start, link = 0, 0

        for i in range(N):
            for j in range(N):

                if visited[i] and visited[j]:
                    start += S[i][j]

                elif not visited[i] and not visited[j]:
                    link += S[i][j]

        ans = min(ans, abs(start-link))

    for i in range(index, N):
        if visited[i]: continue

        visited[i] = 1
        dfs(i+1, count + 1)
        visited[i] = 0

dfs(0, 0)
print(ans)

