x, y, w, h = map(int, input().split())
arr = [x, y, abs(w-x), abs(h-y)]

print(min(arr))
