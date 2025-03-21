from collections import deque

n, m, p = map(int, input().split())
candidates = list(map(int, input().split()))
adj = [[] for _ in range(n + 1)]

for _ in range(p):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start, target, exclude_u, exclude_v):
    distance = [-1] * (n + 1)
    q = deque()
    q.append(start)
    distance[start] = 0
    while q:
        u = q.popleft()
        for v_nei in adj[u]:
            if (u == exclude_u and v_nei == exclude_v) or (u == exclude_v and v_nei == exclude_u):
                continue
            if distance[v_nei] == -1:
                distance[v_nei] = distance[u] + 1
                if v_nei == target:
                    return distance[v_nei]
                q.append(v_nei)
    return -1

min_cycles = []
for mi in candidates:
    min_cycle = float('inf')
    neighbors = adj[mi]
    for v in neighbors:
        path_length = bfs(v, mi, mi, v)
        if path_length != -1:
            cycle_length = 1 + path_length
            if cycle_length >= 2:
                if cycle_length < min_cycle:
                    min_cycle = cycle_length
    if min_cycle != float('inf'):
        min_cycles.append(min_cycle)
    else:
        min_cycles.append(float('inf'))

min_val = min(min_cycles)
result = [candidates[i] for i in range(m) if min_cycles[i] == min_val]
result.sort()

print(len(result))
print(' '.join(map(str, result)))