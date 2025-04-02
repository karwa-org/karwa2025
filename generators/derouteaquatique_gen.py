import heapq, random

def solve(n, m, i_s, j_s, i_t, j_t, lines):
    perturbations = [0] * n*m
    for i,line in enumerate(lines):
        for j,c in enumerate(line):
            if c == 'P': perturbations[i*m+j] = 1
    start, target = i_s*m+j_s, i_t*m + j_t
    dist = [1e18] * n*m
    q, dist[start] = [(0,start)], 0
    while q:
        d, v = heapq.heappop(q)
        #print(f'>> {v}, dist={d}, old_dist={dist[v]}, steps={1 + perturbations[v]*3}')
        if v == target:
            ans = d
            break
        if d > dist[v]: continue
        cost = 1 + perturbations[v]*3
        for u in [(v-1),(v+1),(v+m),(v-m)]:
            if u < 0 or u >= n*m or (abs(u-v) == 1 and u // m != v // m and m != 1): continue
            dd = d + cost
            if dd < dist[u]:
                dist[u] = dd
                heapq.heappush(q,(dd,u))
    return ans


def write(n, m, i_s, j_s, i_t, j_t, lines, name, ans=None):
    with open(f'data/secret/{name}.in', 'w') as f:
        f.write(f'{n} {m}\n{i_s} {j_s} {i_t} {j_t}\n{'\n'.join(lines)}')
    ans_ = solve(n, m, i_s, j_s, i_t, j_t, lines)
    if ans is not None and ans_ != ans:
        print(f'WARNING !!! {name} got {ans_} but it should be {ans}')
    with open(f'data/secret/{name}.ans', 'w') as f:
        f.write(str(ans if ans is not None else ans_))

MINI, MAXI = 1, 700


# VERTICAL LINE
for i in range(15):
    n, m = random.randint(MINI, MAXI), 1
    i_s, j_s, i_t, j_t = 0, 0, n-1, m-1
    lines = ['+' if random.random() < .8 else 'P' for _ in range(n*m)]
    ans = abs(i_s - i_t) + abs(j_s - j_t) + 3 * sum(c == 'P' for c in lines)
    if lines[-1] == 'P': ans -= 3
    write(n, m, i_s, j_s, i_t, j_t, lines, f'random_vertical_line_{i}', ans=ans)


# HORIZONTAL LINE
for i in range(15):
    n, m = 1, random.randint(MINI, MAXI)
    i_s, j_s, i_t, j_t = 0, 0, n-1, m-1
    lines = [''.join(['+' if random.random() < .8 else 'P' for _ in range(n*m)])]
    ans = abs(i_s - i_t) + abs(j_s - j_t) + 3 * sum(c == 'P' for c in lines[0])
    if lines[0][-1] == 'P': ans -= 3
    write(n, m, i_s, j_s, i_t, j_t, lines, f'random_horizontal_line_{i}', ans=ans)


# RANDOM
for density in [.15, .4, .7, .95]:
    for i in range(15):
        n, m = MAXI, MAXI
        i_s, j_s, i_t, j_t = random.randint(n-30, n-1), random.randint(m-30, m-1), random.randint(0, 30), random.randint(0, 30)
        lines = []
        for _ in range(n):
            lines.append(''.join(['+' if random.random() < (1-density) else 'P' for _ in range(m)]))
        write(n, m, i_s, j_s, i_t, j_t, lines, f'random_density{int(density*100)}_{i}')
