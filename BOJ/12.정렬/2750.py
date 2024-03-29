N = int(input())
l = []

for _ in range(N):
    l.append(int(input()))

for i in range(0, N):
    print(min(l))
    l.remove(min(l))

# 버블정렬
''''
N = int(input())

numbers = []

for _ in range(N):
    numbers.append(int(input()))

# Bubble Sort
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

for n in numbers:
    print(n)
'''''

# 삽입정렬
'''''
N = int(input())
nums = []

for _ in range(N) : 
    nums.append(int(input()))

# Insert Sort
for i in range(1, len(nums)) :
    while (i>0) & (nums[i] < nums[i-1]) :
        nums[i], nums[i-1] = nums[i-1], nums[i]

        i -= 1

for n in nums : 
    print(n)
'''''