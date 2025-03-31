n, pos, speeds, target = int(input()), list(map(int, input().split())), list(map(int, input().split())), int(input())
time, ans = 0, 0
while True:
    # Find the closest remaining fish (O(n))
    closest_dist, closest = 1e18, -1
    for i in range(n):
        if 0 <= target-pos[i] < closest_dist:
            closest_dist, closest = target-pos[i], i
    if closest == -1: break # exit if no one
    ans += 1
    # Check each fish that was about to reach before the closest, if yes same group
    delay = closest_dist / speeds[closest]
    for i in range(n):
        if pos[i] <= pos[closest]:
            if (target-pos[i]) / speeds[i] <= delay:
                pos[i] = target+1
print(ans)