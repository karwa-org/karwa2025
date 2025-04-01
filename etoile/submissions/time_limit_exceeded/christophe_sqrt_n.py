n = int(input())
if n < 5: print(0)
else:
    size = 0
    bac = 1
    while bac <= n:
        size += 1
        bac += 4 * size
    print(size - 1)