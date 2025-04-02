import math
from decimal import Decimal, getcontext

getcontext().prec = 50

def result1(n):
    return int((Decimal(2*Decimal(n) - 1).sqrt() - 1) // 2)

def result2(n):
    return math.floor((math.sqrt(2*n-1)-1)/2)

def result3(n):
    low, high, ans = 0, n, 0
    while low <= high:
        mid = (low+high)//2
        res = 2*mid*mid + 2*mid + 1
        if res > n: high = mid-1
        else: low, ans = mid+1, max(ans, mid)
    return ans

def result4(n):
    return int((Decimal(2*Decimal(n) - 1).sqrt() + 1) // 2) - 1

def result5(n):
    return math.floor((math.sqrt(2*n-1)+1)/2) - 1

def result6(n):
    low, high, ans = 0, n, 0
    while low <= high:
        mid = (low+high)//2
        res = 2*mid*mid - 2*mid + 1
        if res > n: high = mid-1
        else: low, ans = mid+1, max(ans, mid)
    return ans-1



import random

def check(n):
    return 2*n*n + 2*n + 1

def write(n, name, idx=None):
    res1 = result1(n)
    res2 = result2(n)
    res3 = result3(n)
    res4 = result4(n)
    res5 = result5(n)
    res6 = result6(n)

    check1, check2, check3, check4, check5, check6 = check(res1), check(res2), check(res3), check(res4), check(res5), check(res6)

    if not (check1 <= n < check(res1+1)): print("Warning1:", n, res1, check1)
    if not (check2 <= n < check(res2+1)): print("Warning2:", n, res2, check2)
    if not (check3 <= n < check(res3+1)): print("Warning3:", n, res3, check3)
    if not (check4 <= n < check(res4+1)): print("Warning4:", n, res4, check4)
    if not (check5 <= n < check(res5+1)): print("Warning5:", n, res5, check5)
    if not (check6 <= n < check(res6+1)): print("Warning6:", n, res6, check6)

    with open(f'star/data/secret/{name}_{idx if idx is not None else n}.in', 'w') as f:
        f.write(str(n))
    with open(f'star/data/secret/{name}_{idx if idx is not None else n}.ans', 'w') as f:
        f.write(str(res1))

write(999999998058150360, "switch")
write(999999998058150361, "switch")
write(int(1e18), "maxi")

for i in range(50):
    n = random.randint(int(1e15), int(1e18))
    write(n, "random", idx=i)
