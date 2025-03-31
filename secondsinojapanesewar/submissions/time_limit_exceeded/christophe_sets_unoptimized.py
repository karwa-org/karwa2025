from collections import deque
n, m, p = map(int, input().split())
candi = list(map(int, input().split()))
adj = [set() for _ in range(n)]
for _ in range(p):
    u, v = map(int, input().split())
    adj[u].add(v)
    adj[v].add(u)

def smallest_cycle_length(start, target):
    q, visited = deque(), {start}
    q.append((1,start))
    while q:
        d, v = q.popleft()
        for u in adj[v]:
            if u not in visited:
                if u == target: return d+1
                q.append((d+1,u))
                visited.add(u)
    return int(1e18)

max_dist, max_paths = int(1e18), set()
for v in candi:
    for u in adj[v]:
        adj[u].remove(v)
        dist = smallest_cycle_length(u, v)
        adj[u].add(v)
        if dist == max_dist:
            max_paths.add(v)
        elif dist < max_dist:
            max_paths, max_dist = {v}, dist
print(f'{len(max_paths)}\n{" ".join(map(str,max_paths))}')