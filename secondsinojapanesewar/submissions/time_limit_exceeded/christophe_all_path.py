n, m, p = list(map(int, input().split()))
candi = list(map(int, input().split()))
adj = [set() for _ in range(n)]
for _ in range(p):
    u, v = list(map(int, input().split()))
    if u == v: continue
    adj[u].add(v)
    adj[v].add(u)

def all_path(start):
    ans = 1e18
    q = [(start,0,set())]
    while q:
        v, d, visited_path = q.pop()
        for u in adj[v]:
            if u == start and u not in visited_path and len(visited_path) != 1:
                ans = min(ans, d+1)
            elif u not in visited_path:
                q.append((u,d+1,visited_path.union({u})))

    return ans

max_dist, max_set = 1e18, set()
for v in candi:
    dist = all_path(v)
    if dist == max_dist:
        max_set.add(str(v))
    elif dist < max_dist:
        max_set = {str(v)}
        max_dist = dist
print(f'{len(max_set)}\n{" ".join(max_set)}')