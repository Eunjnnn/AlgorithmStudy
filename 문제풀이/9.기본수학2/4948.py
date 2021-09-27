def find_prime(a):
    if a == 1:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

all_list = list(range(2, 246912))
left_list = []

for i in all_list :
    if find_prime(i):
        left_list.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in left_list:
        if n < i <= 2 * n:
            count+= 1
    print(count)
    n = int(input())



