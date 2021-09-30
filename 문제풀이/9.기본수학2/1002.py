import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
    R = [distance, r1, r2]
    max_r = max(R)
    R.remove(max_r)
    if distance == 0 and r1 == r2:
        print('-1')
    elif distance == r1 + r2 or max(r1, r2) == distance + min(r1, r2):
        print('1')
    elif max_r > sum(R):
        print('0')
    else:
        print('2')


