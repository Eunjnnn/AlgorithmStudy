T = int(input())

p = [0] * 101
p[1] = 1
p[2] = 1
p[3] = 1

for i in range(0, 98):
    p[i+3] = p[i] + p[i+1]

for i in range(T):
    case = int(input())
    print(p[case])