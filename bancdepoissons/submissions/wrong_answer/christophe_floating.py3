n, pos, speeds, target = int(input()), list(map(int, input().split())), list(map(int, input().split())), int(input())
merged, time, ans = sorted([(pos[i],speeds[i]) for i in range(n)], key=lambda x: x[0], reverse=True), 0, 0
for p, s in merged:
    t = (target-p)/s
    if t >= time: time, ans = t, ans+1
print(ans)