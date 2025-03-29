n = int(input())
elements = list(map(int, input().split()))
prefix_sum = [0] * (n+1)
for i in range(len(elements)):
    prefix_sum[i+1] = prefix_sum[i] + elements[i]

def solve(i,j):
    if i == j:
        return 0
    min_cost = 1e18
    for k in range(i,j):
        min_cost = min(min_cost, solve(i,k) + solve(k+1,j) + prefix_sum[j+1] - prefix_sum[i])
    return min_cost

print(solve(0, n-1))