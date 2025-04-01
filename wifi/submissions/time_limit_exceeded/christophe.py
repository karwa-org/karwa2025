n, q = list(map(int, input().split()))
antennas = list(map(int, input().split()))
for _ in range(q):
    closest = 1e20
    client = int(input())
    for ant in antennas:
        if abs(ant - client) < abs(closest - client): closest = ant
    print(closest)