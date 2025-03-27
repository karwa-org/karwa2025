c = int(input())
start = int(input())
n = int(input())

car = [0]*c
graph = [[] for i in range(c)]
visited = [False]*c
odd_car = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    car[a]+= 1
    car[b]+= 1
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited):
    visited[start] = True
    count = 0
    if car[start]%2 == 1:
        count += 1
    for i in graph[start]:
        if not visited[i]:
            count += bfs(graph, i, visited)
    return count

x = bfs(graph, start, visited)
if x*(x-2) == 0:
    print("Oui")
else:
    print("Non")
