n = int(input())
elements = list(map(int, input().split()))
dp, prefix_sum = [[0]*n for _ in range(n)], [0] * (n+1) # dp[i][j] is the minimal cost to merge from i to j
for i in range(n): # precompute sum of prefixes
    prefix_sum[i+1] = prefix_sum[i] + elements[i]
for l in range(2,n+1):
    for i in range(n-l+1):
        j = i+l-1
        dp[i][j] = 1e18
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + prefix_sum[j+1] - prefix_sum[i])
print(dp[0][n-1])