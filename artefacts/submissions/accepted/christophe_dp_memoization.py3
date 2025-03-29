n = int(input())
elements = list(map(int, input().split()))
MEMO, prefix_sum = [[1e18 for _ in range(n)] for _ in range(n)], [0]*(n+1)
for i in range(len(elements)):
    prefix_sum[i+1] = prefix_sum[i] + elements[i]
def solve(i,j): # usage of @lru_cache(None) is slower
    if MEMO[i][j] != 1e18: return MEMO[i][j]
    ans = 1e18
    if i == j: ans = 0
    else:
        for k in range(i,j):
            ans = min(ans, solve(i,k) + solve(k+1,j) + prefix_sum[j+1] - prefix_sum[i])
    MEMO[i][j] = ans
    return ans
print(solve(0, n-1))