# 체스에서 퀸은 가로, 세로, 대각선 방향으로 끝까지 이동할 수 있다.
# 즉, N개의 퀸을 체스판 위에 올려놓았을 때, 서로 가로, 세로, 대각선 방향으로 겹치면 안된다.


'''
퀸을 한개씩 추가로 놓을 때마다 해당 위치에 퀸이 위치할 수 있는지를 체크하고,
놓을 수 있으면 놓고 다음 퀸의 위치를 탐색한다.
N*N 체스판에 N개의 퀸 놓기를 성공하면 count를 한개 추가하고 탐색을 계속한다.

1. 같은 열인지 확인
· col[i] : i 번째 행에서 퀸이 놓여있는 열의 위치
· col[k] : k 번째 행에서 퀸이 놓여있는 열의 위치
------> col[i]==col[k] 일때 같은 열에 놓이게 되므로 유망하지 않음!

2. 대각선 체크
| col[i] - col[k] | = i - k 인 경우 유망하지 않다.

'''


import sys

# 1. 퀸의 개수 n을 받아오고 퀸의 행의 위치를 저장할 col리스트를 생성한다.
N = int(sys.stdin.readline())
count = 0
col = [0] * N

# 2. 퀸의 위치가 올바른지 확인할 함수를 생성한다.
def isCorrect(i):
    for x in range(i):
        if col[i] == col[x] or abs(col[i] - col[x]) == i-x:
        # 만약 같은 열에 위치하거나 대각선에 위치한다면
            return False
            #올바른 위치가 아니다.
    return True


# 3. i는 0부터 시작해 n이 되면 경우의 수 + 1을 해준다
def nQueens(i):
    global count
    if i == N:      # 만약 퀸의 개수가 n개라면 탈출하면서 경우의 수를 반환
        count += 1
    else:
        for j in range(N):
            col[i] = j  #col[1] = 1-n 까지 1, 1~1, n 까지 반복
            if isCorrect(i):
                nQueens(i + 1)

# 4. nQueens는 0부터 시작하여 count를 반환한다.
nQueens(0)
print(count)