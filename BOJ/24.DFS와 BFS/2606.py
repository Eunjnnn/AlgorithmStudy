from inspect import stack
import sys
from collections import deque


def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            # print(visited)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return len(visited) - 1


num = int(input())
connect = int(input())
d = {}
for _ in range(connect):
    key, val = map(int, sys.stdin.readline().split())
    if key not in d:
        d[key] = list()
    if val not in d:
        d[val] = list()
    d[key].append(val)
    d[val].append(key)

# print(d)
print(BFS(d, 1))
