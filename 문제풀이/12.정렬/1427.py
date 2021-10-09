N = int(input())

N_str = str(N)
li = [0] * len(N_str)

for i in range(len(N_str)):
    li[i] = N_str[i]
    li[i] = int(li[i])

li.sort(reverse=True)
for i in li: print(i, end='')