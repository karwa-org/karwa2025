import bisect

def take_closest(values, target):
    left = 0
    right = len(values) - 1
    while (left < right):
        m = (left + right) //2
        if values[m] == target:
            return values[m]

        if values[m] < target:
            left = m+1
        else:
            right = m-1

    prev = values[left-1] if left != 0 else -1
    current = values[left]
    next = values[left+1] if left != len(values)-1 else -1

    best_dist = abs(target - current)
    best_value = current

    if prev != -1:
        if abs(target - prev) < best_dist:
            best_dist = abs(target - prev)
            best_value = prev

    if next != -1:
        if abs(target - next) < best_dist:
            best_dist = abs(target - next)
            best_value = next

    return best_value


n, q = list(map(int,input().strip().split(" ")))
values = list(map(int,input().strip().split(" ")))
values = sorted(values)

for _ in range(q):
    val = int(input().strip())
    print(take_closest(values, val))