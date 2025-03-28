n, m, p = list(map(int, input().split()))
candi = list(map(int, input().split()))
adj = [set() for _ in range(n)] # set to delete double edges
for _ in range(p):
    u, v = list(map(int, input().split()))
    if u == v: continue # loops
    adj[u].add(v)
    adj[v].add(u)

def bfs(start, target):
    queue, visited, dist = [(start,0)], {start}, 1e17
    while queue:
        v, d = queue.pop()
        if v == target:
            dist = d
            break
        for u in adj[v]:
            if u not in visited:
                queue.append((u,d+1))
                visited.add(u)
    return dist

max_dist, max_set = 1e18, set()
for v in candi:
    for u in adj[v]:
        adj[u].remove(v) # remove u -> v
        dist = bfs(u, v)
        #print(f">> from {v} -> {u}, distance={dist}")
        adj[u].add(v)

        if dist == max_dist:
            max_set.add(str(v))
        elif dist < max_dist:
            max_set = {str(v)}
            max_dist = dist
print(f'{len(max_set)}\n{" ".join(max_set)}')