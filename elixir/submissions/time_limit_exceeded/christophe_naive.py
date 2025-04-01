from itertools import product
from functools import reduce
S, P = map(int, input().split())
count = 0
for comb in product(range(1, S+1), repeat=S): # every partition
    if sum(comb) == S and reduce(lambda x, y: x * y, comb, 1) == P:
        count += 1
print(count)