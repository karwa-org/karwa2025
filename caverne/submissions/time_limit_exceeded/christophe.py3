h, l, p = list(map(int, input().split()))
ceil = [list(map(int, input().split())) for i in range(l)]
floor = [list(map(int, input().split())) for i in range(l)]
cave = 0
for i in range(l):
    for j in range(p):
        for k in range(floor[i][j], h-ceil[i][j]):
            cave += 1 # could create a h*l*p Boolean matrix and put True in i+j*l+k*l*p then sum(cave), but memoryerror
print(cave)
