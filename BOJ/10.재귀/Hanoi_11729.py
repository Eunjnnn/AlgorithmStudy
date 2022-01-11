N = int(input())

def Hanoi(n, a, b, c) :
    if n == 1:
        print(a, c)
    else:
        Hanoi(n-1, a, c, b)
        print(a, c)
        Hanoi(n-1, b, a, c)

count = 1
for i in range(N-1):
    count = count * 2 + 1
print(count)
Hanoi(N, 1, 2, 3)