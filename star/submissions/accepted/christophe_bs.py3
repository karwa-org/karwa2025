n = int(input())
low, high, ans = 0, n, 0
while low <= high:
    mid = (low+high)//2
    res = 2*mid*mid + 2*mid + 1
    if res > n: high = mid-1
    else: low, ans = mid+1, max(ans, mid)
print(ans)