''''
스도쿠는 DFS(깊이 우선 탐색)과 백트래킹(브루트 포스, 전부 탐색)으로 풀 수 있다.

다만 너무 많은 재귀, 검사를 할 것에 대비해 유망한 숫자 검사(is_promising)와 재귀를 최소화 해줄 수 있게(zeros 리스트) 만든다.

pypy로 풀이하였다.
'''

# 1) 0인 부분만을 찾는다.
# 2) 유망한 숫자(해당 칸 안에 들어갈 수 있는 숫자)를 알려줄 is_promising 함수를 만든다
# 2-1) 행, 열, 3*3박스 안에서 검사할 수 있게 만든다.
# 3) 유망한 숫자들을 집어넣는다.
# 4) 다음 0인 부분으로 넘어간다. ( 재귀함수를 호출한다. )
# 5) 해당 부분을 다시 0으로 초기화 시켜 놓는다. ( 4)의 재귀 함수 내부에서 정답이 없을 경우를 고려 )
# 6) 마지막 0까지 모두 넣어봤다면, 출력한다.


# sudoku = [list(map(int, input().split())) for _ in range(9)]
sudoku = []
for i in range(9):
    sudoku.append(list(map(int, input().split())))

# zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))

def is_promising(i, j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])

    # 3 * 3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])
    return promising


flag = False        # 답이 출력되었는가?
def dfs(x):
    global flag

    if flag:    # 이미 답이 출력된 경우
        return

    if x == len(zeros):     # 마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True
        return

    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)

        for num in promising:
            sudoku[i][j] = num  # 유망한 숫자 중 하나를 넣어줌
            dfs(x + 1)  # 다음 0으로 넘어감
            sudoku[i][j] = 0    # 초기화 (정답이 없을 경우를 대비)


dfs(0)