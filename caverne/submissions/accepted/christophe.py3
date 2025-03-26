h,l,p = list(map(int, input().split()))
ceil,floor = [list(map(int, input().split())) for _ in range(l)], [list(map(int, input().split())) for _ in range(l)]
print(h*l*p - sum(min(h, ceil[i][j]+floor[i][j]) for i in range(l) for j in range(p)))