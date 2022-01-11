N , M = map(int, input().split())

s = []

def dfs(first):
    if len(s) == M:
        # print('final: ', s)
        print(' '.join(map(str, s)))
        return

    for i in range(first, N+1):
        if i not in s:
            # print('original: ', s)
            s.append(i)
            # print('s.append(i): ', s)
            dfs(i+1)
            s.pop()
            # print('s.pop(i): ', s)

dfs(1)