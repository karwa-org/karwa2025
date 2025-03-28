from collections import deque
n, m, p = map(int, input().split())
candi = list(map(int, input().split()))
adj = [set() for _ in range(n)] # set to delete double edges
for _ in range(p):
    u, v = map(int, input().split())
    if u == v: continue # loops
    adj[u].add(v)
    adj[v].add(u)

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

max_dist, max_paths = int(1e18), set()
for v in candi:
    for u in adj[v]:
        adj[u].remove(v) # remove u -> v
        dist = smallest_cycle_length(u, v)
        adj[u].add(v)
        if dist == max_dist:
            max_paths.add(str(v))
        elif dist < max_dist:
            max_paths = {str(v)}
            max_dist = dist
print(f'{len(max_paths)}\n{" ".join(max_paths)}')