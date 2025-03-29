n = int(input())
elements = list(map(int, input().split()))
ans = 0
while n > 1:
    best, val_best = -1, 1e18
    for i in range(n-1):
        if elements[i] + elements[i+1] < val_best:
            best, val_best = i, elements[i] + elements[i+1]
    ans += val_best
    elements[best] += elements.pop(best+1)
    n -= 1
print(ans)