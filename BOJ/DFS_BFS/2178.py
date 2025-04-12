N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for n in range(N):
    temp = input()
    for m in range(M):
        maze[n][m] = int(str(temp)[m])

# print(maze)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = [(0, 0)]
answer = 0

while queue:
    x, y = queue.pop(0)

    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0<= mx < N and 0<= my < M:
            if maze[mx][my] == 1:
                maze[mx][my] = maze[x][y] + 1
                queue.append((mx, my))

print(maze[N-1][M-1])