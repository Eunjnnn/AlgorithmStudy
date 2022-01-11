import sys
from collections import Counter

N = int(sys.stdin.readline())
li = []

for _ in range(N):
    li.append(int(sys.stdin.readline()))
sum = 0

# 산술평균
for i in range(len(li)):
    sum += li[i]
print(round(sum/N))

# 중앙값
li.sort()
print(li[len(li)//2])

# 최빈값
mode_dict = Counter(li)
modes = mode_dict.most_common()

if len(li) > 1:
    if modes[0][1] == modes[1][1]:
        mod = modes[1][0]
    else:
        mod = modes[0][0]
else:
    mod = modes[0][0]

print(mod)

# 범위
print(max(li) - min(li))