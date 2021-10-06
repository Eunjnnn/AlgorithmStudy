N = int(input())
count = 0
end = 666

while True:
    if '666' in str(end):
        count += 1
    if count == N:
        print(end)
        break
    end += 1