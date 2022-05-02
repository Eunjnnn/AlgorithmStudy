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
    return " ".join(str(i) for i in visited)


def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        # print(stack)
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)


# node, branch, first node
n, m, s = map(int, sys.stdin.readline().split())
print('n:', n, 'm:', m, 's:', s)
d = {}
for _ in range(m):
    key, val = map(int, sys.stdin.readline().split())
    if key not in d:
        d[key] = list()
    if val not in d:
        d[val] = list()
    d[key].append(val)
    d[val].append(key)

# print(d)

print(DFS(d, s))
print(BFS(d, s))
