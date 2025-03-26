from functools import reduce
S, P = list(map(int, input().split()))
MEM = {} # Alternatively: use @lru_cache(None) from functools on get_all
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
print(sum(reduce(lambda x,y: x*y, subset) == P for subset in get_all(S)))