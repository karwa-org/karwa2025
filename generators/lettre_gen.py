import random
from collections import defaultdict

def solve(c, d, r, edges):
    degrees = defaultdict(lambda: 0)
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
        degrees[a] += 1
        degrees[b] += 1
    queue, odd, visited = [d], degrees[d] & 1, {d}
    while queue and odd < 3:
        curr = queue.pop()
        for succ in adj[curr]:
            if succ not in visited:
                queue.append(succ)
                visited.add(succ)
                odd += degrees[succ] & 1
    return "Oui" if odd < 3 else "Non"



MINI = 10**4
MAXI = 10**5

for i in range(30,35):
    c = MINI
    r = MAXI
    d = random.randint(0, c-1)

    edges = [(random.randint(0, c-1),random.randint(0, c-1)) for _ in range(r)]

    ans = solve(c, d, r, edges)

    with open(f"data/secret/random_{i}.in", "w") as f:
        f.write(f"{c}\n{d}\n{r}\n{"\n".join(map(lambda x: f"{x[0]} {x[1]}", edges))}")
    with open(f"data/secret/random_{i}.ans", "w") as f:
        f.write(ans)


# PATH
c = MAXI-5
d = 0

edges = [(i,i+1) for i in range(5, c-1)]
edges += [(0,1),(1,2),(1,3),(1,4),(1,0)]

r = len(edges)

ans = solve(c, d, r, edges)

with open(f"data/secret/path_{MAXI}_out.in", "w") as f:
    f.write(f"{c}\n{d}\n{r}\n{"\n".join(map(lambda x: f"{x[0]} {x[1]}", edges))}")
with open(f"data/secret/path_{MAXI}_out.ans", "w") as f:
    f.write(ans)
