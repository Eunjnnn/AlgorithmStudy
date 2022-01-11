coordx1, coordy1 = map(int, input().split())
coordx2, coordy2 = map(int, input().split())
coordx3, coordy3 = map(int, input().split())

if coordx1 == coordx2:
    print(coordx3, end=' ')
elif coordx1 == coordx3:
    print(coordx2, end=' ')
else:
    print(coordx1, end=' ')

if coordy1 == coordy2:
    print(coordy3)
elif coordy1 == coordy3:
    print(coordy2)
else:
    print(coordy1)

'''
x_ = []
y_ = []
for i in range(3):
        x, y = map(int, input().split())
        x_.append(x)
        y_.append(y)
for i in range(3):
        if x_.count(x_[i]) == 1:
                x = x_[i]
        if y_.count(y_[i]) == 1:
                y = y_[i]
print(x, y)
'''