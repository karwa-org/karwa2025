import random
from functools import reduce

def get_all(n, maxi=None):
    if n == 0: return [()]
    if maxi is None: maxi = n
    key = (n, maxi)
    if key in MEM: return MEM[key]
    result = []
    for i in range(1, min(n,maxi)+1):
        for subset in get_all(n-i, i):
            result.append((i,) + subset)
    MEM[key] = result
    return result

nbr = 8
while nbr < 9:
    MEM = {}
    S, P = 41, random.randint(10**2, 10**6)
    ans1 = sum(reduce(lambda x,y: x*y, subset) == P for subset in get_all(S))
    ans2 = sum(reduce(lambda x,y: x*y, subset) == P for subset in get_all(42))

    if ans1 != ans2:
        print("FOUND", nbr)
        with open(f'elexir/data/secret/{nbr}_nonzero.in', 'w') as f:
            f.write(f"{S} {P}")
        with open(f'elexir/data/secret/{nbr}_nonzero.ans', 'w') as f:
            f.write(f"{ans1}")
        nbr += 1
