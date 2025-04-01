n, q = list(map(int, input().split()))
antennas = sorted(list(map(int, input().split())))
for _ in range(q):
    client, low, high = int(input()), 0, n-1
    while low <= high:
        mid = (low+high)//2
        if client > antennas[mid]: low = mid+1
        elif client < antennas[mid]: high = mid-1
        else: break
    if client == antennas[mid]: print(client)
    elif low >= n: print(antennas[-1])
    elif high < 0: print(antennas[0])
    else: print(antennas[low] if abs(antennas[low] - client) < abs(antennas[high] - client) else antennas[high])