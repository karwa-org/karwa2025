import random

def solve(n, elements):
    dp, prefix_sum = [[0]*n for _ in range(n)], [0] * (n+1) # dp[i][j] is the minimal cost to merge from i to j
    for i in range(n): # precompute sum of prefixes
        prefix_sum[i+1] = prefix_sum[i] + elements[i]
    for l in range(2,n+1):
        for i in range(n-l+1):
            j = i+l-1
            dp[i][j] = 1e18
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + prefix_sum[j+1] - prefix_sum[i])
    return dp[0][n-1]

def write(n, elements, name):
    print("Starting", name)
    ans = solve(n, elements)
    print("Writing", name)
    with open(f"data/secret/{name}.in", "w") as f:
        f.write(f"{n}\n{' '.join(map(str,elements))}\n")
    with open(f"data/secret/{name}.ans", "w") as f:
        f.write(f"{ans}\n")

for i in range(10):
    n = 300
    elements = [random.randint(1, int(1e9)) for _ in range(n)]
    write(n, elements, f"random_{i}")

n = 300
elements = [int(1e9) for _ in range(n)]
write(n, elements, f"full_max")

n = 300
elements = [1 for _ in range(n)]
write(n, elements, f"full_1")

n = 300
elements = [(i+1)*100 for i in range(n)]
write(n, elements, f"increasing")
elements = [(i+1)*100 for i in range(n-1,-1,-1)]
write(n, elements, f"decreasing")
elements = [(i+1)*1000 if i < 150 else (n-i+1)*1000 for i in range(n-1,-1,-1)]
write(n, elements, f"peak")

for i in range(10):
    n = random.randint(200, 300)
    elements = [random.randint(10**5, int(1e9)) for _ in range(n)]
    write(n, elements, f"random_high_{i}")