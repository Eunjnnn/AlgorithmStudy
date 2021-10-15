N , M = map(int, input().split())

s = []

def dfs(start):
    if len(s) == M:
        # print('final: ', s)
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        # print('original: ', s)
        s.append(i)
        # print('s.append(i): ', s)
        dfs(i)
        s.pop()
        # print('s.pop(i): ', s)

dfs(1)