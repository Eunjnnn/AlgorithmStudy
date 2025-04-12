
N, M, V = map(int, input().split())
nodes = [[0] * (N+1) for _ in range(N+1)]

for m in range(M):
    node1, node2 = map(int, input().split())
    nodes[node1][node2] = 1
    nodes[node2][node1] = 1

visited_dfs = [0] * len(nodes)
visited_bfs = [0] * len(nodes)

result_dfs = []
result_bfs = []


def DFS(graph, root):

    if visited_dfs[root] == 0:
        print(root, end = ' ')
        visited_dfs[root] = 1
    
    for g in range(len(graph[root])):
        if graph[root][g] == 1 and visited_dfs[g] == 0:
            DFS(graph, g)

    return result_dfs



def BFS(graph, root):

    queue = [root]

    if visited_bfs[root] == 0:
        visited_bfs[root] = 1
    

    while queue:
        node = queue.pop(0)
        print(node, end=' ')
        for g in range(len(graph[node])):
            if graph[node][g] == 1 and visited_bfs[g] == 0:
                queue.append(g)
                visited_bfs[g] = 1

    return result_dfs


# DFS
DFS(nodes, V)
print()
# BFS
BFS(nodes, V)





