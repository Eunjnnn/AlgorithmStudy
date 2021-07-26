
str = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
time = 0
var = var_input('')
for i in range(len(var)):
    for a in str:
        if var[i] in a:
            time += str.index(a) + 3

print(time)
