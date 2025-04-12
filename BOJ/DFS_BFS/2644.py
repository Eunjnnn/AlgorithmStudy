n = int(input())
S, E = map(int, input().split())
m = int(input())
dict = {}
for i in range(m):
    p, c = map(int, input().split())
    if p not in dict.keys():
        dict[p] = list()
    if c not in dict.keys():
        dict[c] = list()
    dict[p].append(c)
    dict[c].append(p)

# print(dict)

visited = []
result = []
def dfs(root, cnt):
    # print(root, cnt)
    cnt += 1
    
    if root not in visited:
        visited.append(root)
        if root == E:
            result.append(cnt)

    for i in range(len(dict[root])):
        if dict[root][i] not in visited:
            dfs(dict[root][i], cnt)

    return result

num_result = dfs(S, 0)
# print(num_result)
if len(num_result) == 0:
    print(-1)
else:
    print(num_result[0] -1)

