# Counting Sort

import sys

arr = [0 for _ in range(10001)]

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1

for i in range(1, 10001):
    count = arr[i]
    for _ in range(count):
        print(i)
