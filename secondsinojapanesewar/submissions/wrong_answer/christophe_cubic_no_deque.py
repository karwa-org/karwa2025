from collections import deque
n, m, p = map(int, input().split())
candi = list(map(int, input().split()))
adj = [[] for _ in range(n)]
for _ in range(p):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start, target):
    queue, visited, dist = [(start,0)], [False]*n, 1e17
    visited[start] = True
    while queue:
        v, d = queue.pop()
        if v == target:
            dist = d
            break
        for u in adj[v]:
            if not visited[u]:
                queue.append((u,d+1))
                visited[u] = True
    return dist

max_dist, max_paths = int(1e18), []
for v in candi:
    found = False
    for u in adj[v]:
        adj[u].remove(v)
        dist = bfs(u, v)
        adj[u].append(v)
        if dist == max_dist and not found:
            found = True
            max_paths.append(v)
        elif dist < max_dist:
            max_paths, max_dist, found = [v], dist, True
print(f'{len(max_paths)}\n{" ".join(map(str,max_paths))}')