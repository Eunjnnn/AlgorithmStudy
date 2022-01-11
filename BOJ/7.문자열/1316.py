num = int(input())

group = 0
for _ in range(num):
    str = input()
    error = 0
    for i in range(len(str)-1):
        if str[i] != str[i+1]:
            new_str = str[i+1:]
            if new_str.count(str[i]) > 0:
                error += 1
    if error == 0:
        group += 1
print(group)
