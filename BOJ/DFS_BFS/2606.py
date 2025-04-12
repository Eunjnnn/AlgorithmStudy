num = int(input())
pairs = int(input())

graph = [[0] * (num+1) for _ in range(num+1)]

for i in range(pairs):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)
visited = []

def dfs(graph, root):
    if root not in visited:
        visited.append(root)
    

    for g in range(len(graph[root])):
        if graph[root][g] == 1 and (g not in visited):
            dfs(graph, g)
    
    return len(visited) -1


print(dfs(graph, 1))