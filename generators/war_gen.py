import numpy as np
from collections import deque
import random

def solve(n, m, p, candidates, edges):
    adj = [[] for _ in range(n + 1)]
    for u, v in edges:
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
    if min_val == float('inf'):
        return None
    result = [candidates[i] for i in range(m) if min_cycles[i] == min_val]
    result.sort()

    return result


def write(n, m, p, candidates, edges, result, name):
    #print("Solving...")
    #result = solve(n, m, p, candidates, edges)
    print("Writing !")
    #if len(result) == 0:
    #    print("ERROR WARNING, result empty")
    with open(f"data/secret/{name}.in", "w") as f:
        f.write(f"{n} {m} {p}\n{' '.join(map(str,candidates))}\n{'\n'.join(map(lambda x: f'{x[0]} {x[1]}', edges))}\n")
    with open(f"data/secret/{name}.ans", "w") as f:
        f.write(f"{len(result)}\n{' '.join(map(str,result))}\n")


def generate_unique_pairs(start, end, num):
    all_pairs = [(i, j) for i in range(start, end + 1) for j in range(i + 1, end + 1)]
    chosen_pairs = np.random.choice(len(all_pairs), size=num, replace=False)
    return [all_pairs[i] for i in chosen_pairs]


for i in range(10):
    print("generating", i)
    failed = True
    while failed:
        n, m, p = random.randint(1, 301), random.randint(1, 301), random.randint(1, 301)
        try:
            print("retry")
            edges = generate_unique_pairs(0, n-1, p)
            candidates = list(np.random.choice(np.arange(0, n), size=m, replace=False))
            failed = False
        except(ValueError):
            failed = True
        if not failed:
            print("Solving...")
            result = solve(n, m, p, candidates, edges)
            if result is None:
                failed = True
    write(n,m,p,candidates,edges,result,f"random_{i}")