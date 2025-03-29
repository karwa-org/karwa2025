from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
def dfs(curr, visited):
    visited.add(curr)
    odd = degrees[curr] & 1
    for succ in adj[curr]:
        if succ not in visited:
            odd += dfs(succ, visited)
            if odd >= 3:
                return odd
    return odd
c, d, r = int(input()), int(input()), int(input())
adj, degrees = defaultdict(set), defaultdict(int)
for _ in range(r):
    a, b = map(int, input().split())
    adj[a].add(b)
    adj[b].add(a)
    degrees[a] += 1
    degrees[b] += 1
visited = set()
odd = dfs(d, visited)
print("Oui" if odd < 3 else "Non")