from collections import defaultdict
c, d, r, adj, degrees = int(input()), int(input()), int(input()), defaultdict(set), defaultdict(lambda: 0)
for _ in range(r):
    a, b = list(map(int, input().split()))
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
print("Oui" if odd < 3 else "Non")