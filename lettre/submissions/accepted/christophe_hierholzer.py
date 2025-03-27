from collections import defaultdict, deque
def find_connected_component(start, adj):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for u in adj[node]:
                if u not in visited:
                    stack.append(u)
    return visited
def find_eulerian_path(component, adj): # Hierholzer Algorithm
    graph = {node: list(adj[node]) for node in component}
    odd_degree_nodes = [node for node in component if len(graph[node]) % 2 == 1]
    if len(odd_degree_nodes) not in [0, 2]:
        return None
    start = odd_degree_nodes[0] if odd_degree_nodes else component.pop()
    stack = [start]
    path = deque()
    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            graph[v].remove(u)
            stack.append(v)
        else:
            path.appendleft(stack.pop())
    return list(path)
c, d, r = int(input()), int(input()), int(input())
adj = defaultdict(list)
for _ in range(r):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
component = find_connected_component(d, adj)
path = find_eulerian_path(component, adj)
if path: print("Oui")
else: print("Non")
