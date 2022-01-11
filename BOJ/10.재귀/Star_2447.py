# 별 그리는 재귀함수
def star(n):
    global Maps

    if n == 3:
        Maps[0][:3] = Maps[2][:3] = [1] * 3
        Maps[1][:3] = [1, 0, 1]
        return

    a = n // 3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Maps[a*i + k][a*j:a*(j+1)] = Maps[k][:a]        # 핵심 아이디어


N = int(input())

Maps = [ [0 for i in range(N)] for i in range(N) ]              # 매트릭스 만들기
'''''
a = [[0]*3 for _ in range(3)]
print(a)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''''

star(N)

for i in Maps:
    for j in i:
        if j:
            print('*', end= '')             # 1은 '별' 0은 '빈칸'
        else:
            print(' ', end= '')
    print()


'''''
def draw_star(n):
    mat = [ ]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            mat.append(n [i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            mat.append(n[i % len(n)] * 3)
    return list(mat)

star = ['***', '* *', '***']
N = int(input())
k = 0
while N != 3:
    N = int(N/3)
    k += 1

for i in range(k):
    star = draw_star(star)
for i in star:
    print(i)
'''''