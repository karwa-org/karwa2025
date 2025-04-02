import random

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

def solve(n, q, values, queries):
    values = sorted(values)
    return [take_closest(values, val) for val in queries]

def write(n, q, values, queries, name):
    ans = solve(n, q, values, queries)
    with open(f"data/secret/{name}.in", "w") as f:
        f.write(f"{n} {q}\n{' '.join(map(str,values))}\n{'\n'.join(map(str,queries))}\n")
    with open(f"data/secret/{name}.ans", "w") as f:
        f.write(f"{'\n'.join(map(str,ans))}\n")

for i in range(6):
    print(f"random_{i}")
    n, q = random.randint(1, 10**5), random.randint(1, 10**5)
    values, queries = [1,1], [1,1]
    while len(values) != len(set(values)):
        values = [random.randint(1, 10**18) for _ in range(n)]
    while len(queries) != len(set(queries)):
        queries = [random.randint(1, 10**18) for _ in range(q)]
    write(n, q, values, queries, f"random_{i}")

for a in range(6):
    print(f"increasing_random_{a}")
    n, q = random.randint(10**4,10**5), random.randint(10**4,10**5)
    exp = random.randint(2,3)
    values = [(i+1)**(exp) for i in range(n)]
    maxi = max(values)
    queries = [1,1]
    while len(queries) != len(set(queries)):
        queries = [random.randint(0, maxi) for i in range(q)]
    random.shuffle(values)
    random.shuffle(queries)
    write(n, q, values, queries, f"increasing_random_{a}")


for a in range(6):
    print(f"peak_random_{a}")
    n, q = random.randint(10**4,10**5), random.randint(10**4,10**5)

    values = [1,1]
    while len(values) != len(set(values)):
        print(a, len(values), len(set(values)))
        numbers = random.sample(range(0, 10**18), n)
        numbers.sort()
        first_half = numbers[:n//2]
        second_half = numbers[n//2:][::-1]
        values = first_half + second_half
    print(a, len(values), len(set(values)))

    maxi = max(values)
    queries = [1,1]
    while len(queries) != len(set(queries)):
        queries = [random.randint(1, maxi) for _ in range(q)]
    random.shuffle(values)
    random.shuffle(queries)
    write(n, q, values, queries, f"peak_random_{a}")
