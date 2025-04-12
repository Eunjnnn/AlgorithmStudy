N = int(input())
map = [[0]*N for _ in range(N)]

for i in range(N):
    temp = input()
    for j in range(N):
        map[i][j] = int(str(temp)[j])

# print(map)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS
def bfs(graph, root):
    queue = [root]
    count = 1    

    while queue:
        x, y = queue.pop(0)
        graph[x][y] = 0

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < N and 0 <= my < N:
                if map[mx][my] == 1:
                    count += 1
                    map[mx][my] = 0
                    queue.append((mx, my))


    return count


# BFS
# cnt = []
# for i in range(N):
#     for j in range(N):
#         if map[i][j] == 1:
#             cnt.append(bfs(map, (i, j)))

# cnt.sort()
# print(len(cnt))
# for i in range(len(cnt)):
#     print(cnt[i])


# DFS
def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    
    if map[x][y] == 1:
        global cnt
        cnt += 1
        map[x][y] = 0

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            dfs(mx, my)
        return True
    return False

# DFS
cnt = 0
result = 0
num = []

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            num.append(cnt)
            result += 1
            cnt = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])

