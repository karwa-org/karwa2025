import heapq
n, m = map(int, input().split())
i_s, j_s, i_t, j_t = map(int, input().split())
perturbations = [0] * n*m # 0 if perturbation, 1 otherwise
for i in range(n):
    for j,c in enumerate(input()):
        if c == 'P': perturbations[i*m+j] = 1
start, target = i_s*m+j_s, i_t*m+j_t
dist = [1e18] * (n*m)
q, dist[start] = [(0,start)], 0
while q: # dijkstra algorithm
    d, v = heapq.heappop(q)
    if v == target:
        ans = d
        break
    if d > dist[v]: continue
    dd = d + 1 + perturbations[v]*3
    for u in [(v-1),(v+1),(v+m),(v-m)]: # compute adjacent list on the fly
        if not (0 <= u < n*m) or (abs(u-v) == 1 and u // m != v // m and m != 1): continue
        if dd < dist[u]:
            dist[u] = dd
            heapq.heappush(q,(dd,u))
print(ans)