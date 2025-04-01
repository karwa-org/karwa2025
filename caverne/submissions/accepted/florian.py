h, l, p = list(map(int, input().split()))

ceil = [list(map(int, input().split())) for i in range(l)]
floor = [list(map(int, input().split())) for i in range(l)]

vol = h*l*p
cobble = 0

for i in range(l):
    for j in range(p):
        cobble += min(h, ceil[i][j]+floor[i][j])
print(vol - cobble)
