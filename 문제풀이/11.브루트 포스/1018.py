N, M = map(int, input().split())
chess = list()
for i in range(N):
    chess.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j + 8):
                if (k+l) % 2 == 0:
                # 행과 열의 인덱스의 합이 짝수인경우, 일정한 한 색을 가지게 되고, 홀수인 경우에도, 다른 일정한 한 색을 가지게 된다.
                # 0(짝)  1(홀)  2(짝)  3(홀)
                # 1(홀)  2(짝)  3(홀)  4(짝)
                # 2(짝)  3(홀)  4(짝)  5(홀)
                # 3(홀)  4(짝)  5(홀)  6(짝)

                    if chess[k][l] != 'W':
                        first_W = first_W + 1
                    if chess[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if chess[k][l] != 'B':
                        first_W = first_W + 1
                    if chess[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)

print(min(repair))
