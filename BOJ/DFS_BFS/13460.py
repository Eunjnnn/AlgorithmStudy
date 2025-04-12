N, M = map(int, input().split())
board = [[] for _ in range(N)]

for n in range(N):
    m = str(input())
    board[n] = list(m)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)


print(red, blue)

visited = []

def move(x, y, dx, dy):
    cnt = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt 


def bfs(R, B):
    rx, ry = R
    bx, by = B
    queue = [(rx, ry, bx, by, 1)]
    visited.append((rx, ry, bx, by))

    while queue:
        latest = queue.pop(0)
        nrx, nry, nbx, nby, depth = latest

        if depth > 10:
            break

        for i in range(4):
            mrx, mry, rcnt = move(nrx, nry, dx[i], dy[i])
            mbx, mby, bcnt = move(nbx, nby, dx[i], dy[i])

            if board[mbx][mby] == "O":
                continue

            if board[mrx][mry] == "O":
                print(depth)
                return
            
            if mrx == mbx and mry == mby:
                if rcnt > bcnt:
                    mrx -= dx[i]
                    mry -= dy[i]
                else:
                    mbx -= dx[i]
                    mby -= dy[i]
            
            if (mrx, mry, mbx, mby) not in visited:
                visited.append((mrx, mry, mbx, mby))
                queue.append((mrx, mry, mbx, mby, depth+1))
    
    print(-1)

bfs(red, blue)

    


