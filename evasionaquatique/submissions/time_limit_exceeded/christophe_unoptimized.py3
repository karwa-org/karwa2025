import heapq
from collections import defaultdict
n, m = map(int, input().split())
i_s, j_s, i_t, j_t = map(int, input().split())

perturbations = set()
for i in range(n):
    for j,c in enumerate(input()):
        if c == 'P':
            perturbations.add((i,j))

adj = defaultdict(list) # compute transitions on the fly to improve by .8s
for i in range(n):
    for j in range(m):
        if i > 0: adj[(i,j)].append((i-1,j))
        if i < n-1: adj[(i,j)].append((i+1,j))
        if j > 0: adj[(i,j)].append((i,j-1))
        if j < m-1: adj[(i,j)].append((i,j+1))

start, target = (i_s, j_s), (i_t, j_t)
dist = defaultdict(lambda: 1e18)
q, dist[start] = [(0,start)], 0
while q:
    d, (i,j) = heapq.heappop(q)
    if (i,j) == target:
        ans = d
        break
    if d > dist[(i,j)]: continue
    dd = d + 1
    if (i,j) in perturbations: dd += 3
    for (ii,jj) in adj[(i,j)]:
        if dd < dist[(ii,jj)]:
            dist[(ii,jj)] = dd
            heapq.heappush(q,(dd,(ii,jj)))
print(ans)