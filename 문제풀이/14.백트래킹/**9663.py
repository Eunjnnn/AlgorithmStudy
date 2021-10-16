# 체스에서 퀸은 가로, 세로, 대각선 방향으로 끝까지 이동할 수 있다.
# 즉, N개의 퀸을 체스판 위에 올려놓았을 때, 서로 가로, 세로, 대각선 방향으로 겹치면 안된다.

# 퀸들이 서로 공격하지 못하게 하기 위해서는 같은 줄(가로줄이던, 세로줄이던)에 있을 수 없는데, 이를 이용할 수 있었다.
# 요소의 개수가 N인 list를 이용하여 각 요소는 해당 열의 퀸의 위치를 표시하도록 하였다. (퀸은 한개의 열에 한개만 있을 수 있으므로) ==> visited
# 또한 해당 행에 퀸이 존재하는지를 표시하는 list를 이용하고, 서로 대각선 방향으로 겹치는지 체크하는 함수를 이용하였다.

'''
퀸을 한개씩 추가로 놓을 때마다 해당 위치에 퀸이 위치할 수 있는지를 체크하고,
놓을 수 있으면 놓고 다음 퀸의 위치를 탐색한다.
N*N 체스판에 N개의 퀸 놓기를 성공하면 count를 한개 추가하고 탐색을 계속한다.
'''


import sys

n = int(sys.stdin.readline())
board = [0] * n
ans_count = 0
visited = [False] * n  # n번째 열에 퀸이 있는지를 표시하는 list

def check(x):   # 기존에 있는 퀸들과 대각선 방향으로 겹치는 퀸이 있는지를 확인
    for i in range(x):
        if abs(board[x] - board[i]) == x - i:
        # 값이 0이라면 퀸이 자리에 없는 의미(처음에 0으로 초기화 해놨기 때문)에
        # => 퀸이
            return False
    return True

def n_queen(x):     # dfs
    global ans_count
    if x == n:
        ans_count += 1
        return
    for i in range(n):
        if visited[i]:  # i번째 열에 퀸이 있을 경우 continue
            continue

        board[x] = i
        if check(x):
            visited[i] = True
            n_queen(x+1)
            visited[i] = False

n_queen(0)
print(ans_count)



