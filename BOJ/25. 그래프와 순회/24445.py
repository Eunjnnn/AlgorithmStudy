# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.setrecursionlimit(10**5)

n, m, r = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
order = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort(reverse=True)
# print(graph)    # [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]


cnt = 1

queue = deque([r])

while queue:
    node = queue.popleft()
    visited[node] = 1
    if order[node] == 0:
        order[node] = cnt
        cnt += 1

    for i in graph[node]:
        if not visited[i]:
            queue.append(i)
            visited[i] = 1

for i in range(1, len(order)):
    print(order[i])
