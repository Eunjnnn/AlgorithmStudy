'''''
1. visited (탐사 했는지 여부)

2. output (탐사 내용)

3. 재귀 함수 시

- 탈출 조건 : Depth가 M일 때

- 탐사를 안했을 경우 진행

- Depth 탐색 전 : 탐사 시작(중복 제거), 탐사 내용 append

- Depth 탐색 후 : 다음 탐사 준비, 탐사 내용 pop
'''''

N , M = map(int, input().split())

visited = [False] * N   # 탐사 여부 check
output = []    # 출력 내용

def solve(depth, N, M):
    if depth == M:      # 탈출 조건
        print(' '.join(map(str, output)))     #list를 str으로 합쳐 출력
        return
    for i in range(len(visited)):       # 탐사 check 하면서
        if not visited[i]:      # 탐사 안했다면
            visited[i] = True   # 탐사 시작(중복 제거)
            output.append(i+1)  # 탐사 내용
            solve(depth+1, N, M)  # 깊이 우선 탐색
            visited[i] = False  # 깊이 탐사 완료
            output.pop()  # 탐사 내용 제거

solve(0, N, M)
