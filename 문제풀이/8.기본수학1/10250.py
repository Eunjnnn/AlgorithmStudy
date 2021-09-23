test = int(input())

for i in range(test):
    h, w, n = map(int, input().split() )

    units = n // h + 1
    hund = n % h
    if n % h == 0:
        units = n//h
        hund = h
    print(f'{hund * 100 + units}')
