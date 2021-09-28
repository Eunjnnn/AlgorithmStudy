while True:
    tri = list(map(int, input().split()))
    max_len = max(tri)
    if sum(tri) == 0:
        break
    tri.remove(max_len)
    if tri[0] ** 2 + tri[1] ** 2 == max_len ** 2:
        print('right')
    else:
        print('wrong')

