from collections import deque
n, m, p = map(int, input().split())
candi = list(map(int, input().split()))
adj = [[] for _ in range(n)] # list instead sets, gain of 0.4s
for _ in range(p):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
def smallest_cycle_length(start, target):
    q, d = deque(), [-1 for _ in range(n)]
    q.append(start)
    d[start] = 1
    while q:
        v = q.popleft()
        for u in adj[v]:
            if d[u] == -1:
                d[u] = d[v] + 1
                if u == target: return d[u]
                q.append(u)
    return int(1e18)
max_dist, max_paths = int(1e18), []
for v in candi:
    found = False
    for u in adj[v]:
        adj[u].remove(v) # remove u -> v
        dist = smallest_cycle_length(u, v)
        adj[u].append(v)
        if dist == max_dist and not found:
            found = True
            max_paths.append(v)
        elif dist < max_dist:
            max_paths, max_dist, found = [v], dist, True
print(f'{len(max_paths)}\n{" ".join(map(str,max_paths))}')