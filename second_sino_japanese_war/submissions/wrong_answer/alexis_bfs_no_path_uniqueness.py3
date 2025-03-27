#
# Solution en O(m*p) avec un bfs
# @EXPECTED_RESULTS@: CORRECT
#

import collections

INF = 1e18+1

def girth(adj, source):
    distance = [INF for i in range(len(adj))]
    distance[source] = 0

    parent = [-1 for i in range(len(adj))]

    ans = INF

    queue = []
    queue.append(source)
    while(len(queue) > 0):
        current = queue.pop(0)
        for v in adj[current]:
            if distance[v] == INF:
                distance[v] = distance[current] + 1
                parent[v] = current
                queue.append(v)
            elif v != parent[current] and current != v:
                ans = min(ans, distance[current] + distance[v] + 1)
    return ans


def solve():
    n, m, p = list(map(int,input().split(" ")))

    candidates = list(map(int, input().split(" ")))

    adj = [[] for _ in range(n)]

    for _ in range(p):
        u, v = list(map(int, input().split(" ")))
        adj[u].append(v)
        adj[v].append(u)

    best_girth = INF

    anss = collections.defaultdict(list)
    for c in candidates:
        g = girth(adj, c)
        anss[g].append(c)
        if g < best_girth:
            best_girth = g

    print(len(anss[best_girth]))
    print(" ".join(list(map(str,anss[best_girth]))))

solve()