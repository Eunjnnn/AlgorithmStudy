N = int(input())
l = []

for _ in range(N):
    l.append(int(input()))

for i in sorted(l):
    print(i)