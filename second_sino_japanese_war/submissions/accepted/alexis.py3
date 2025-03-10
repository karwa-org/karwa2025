import sys
from collections import deque, defaultdict

INF = float('inf')

def girth(adj, source):
    d = [INF] * len(adj)
    d[source] = 0
    q = deque([source])
    shortest_cycle = INF
    p = [-1] * len(adj)
    
    while q:
        current = q.popleft()
        found_cycle = False
        
        for v in adj[current]:
            if v == p[current]:
                continue
            if current == v:
                continue
            
            if d[v] == INF:
                p[v] = current
                d[v] = d[current] + 1
                q.append(v)
            else:
                path = {}
                current_node = current
                while current_node != source:
                    path[current_node] = True
                    current_node = p[current_node]
                
                is_distinct_path = True
                current_node = v
                while current_node != source:
                    if current_node in path:
                        is_distinct_path = False
                        break
                    current_node = p[current_node]
                
                if not is_distinct_path:
                    continue
                
                shortest_cycle = min(shortest_cycle, d[current] + d[v] + 1)
                found_cycle = True
                continue
        
        if found_cycle:
            return shortest_cycle
    
    return shortest_cycle

def solve():
    n, m, p = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n)]
    candidates = list(map(int, sys.stdin.readline().split()))
    degree = [0] * n
    
    for _ in range(p):
        u, v = map(int, sys.stdin.readline().split())
        degree[u] += 1
        degree[v] += 1
        adj[u].append(v)
        adj[v].append(u)
    
    ans = INF
    best_idx = -1
    all_ans = defaultdict(list)
    
    for c in candidates:
        if degree[c] <= 1:
            continue
        g = girth(adj, c)
        all_ans[g].append(c)
        if g < ans:
            ans = g
            best_idx = c
    
    print(len(all_ans[ans]))
    print(" ".join(map(str, all_ans[ans])))

if __name__ == "__main__":
    solve()
