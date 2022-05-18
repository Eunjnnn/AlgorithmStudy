# -*- coding: utf-8 -*-
import sys
from collections import deque
sys.setrecursionlimit(10**5)

n, m, r = map(int, sys.stdin.readline().split())
visited = [0] * (n+1)
order = [0] * (n+1)
# print('visited:', visited)
# print('order:', order)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()
# print(graph)    # [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]

# ㅈㅐ구ㅣ
# def dfs(start):
#     # print(start, end=' ')
#     visited[start] = True
#     order[start-1] = max(order) + 1
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i)
#             visited[i] = True

cnt = 1

stack = deque()
stack.append(r)

while stack:
    node = stack.pop()
    visited[node] = 1
    if order[node] == 0:
        order[node] = cnt
        cnt += 1

    for i in graph[node]:
        if not visited[i]:
            stack.append(i)

for i in range(1, len(order)):
    print(order[i])
