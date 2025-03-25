"""
1 1 ^n = F_n+1 F_n
1 0      F_n   F_n-1
"""

fiblist = [1,2]

for n in range(2, 120):
    fiblist.append(fiblist[n-2]+fiblist[n-1])

import math

"""
def getFibEncoding(n)
    rest = n
    res = ''
    for i in range(len(fiblist)-1,-1,-1):
        if fiblist[i] <= rest:
            res = '1' + res
            rest -= fiblist[i]
        else:
            res = '0' + res
    return int(res[::-1])
"""
def getFibEncoding(n):
    res = 0
    rest = n
    res_ = ''
    for i in range(len(fiblist)-1,-1,-1):
        if fiblist[i] <= rest:
            res += i+1
            res_ = '1' + res_
            rest -= fiblist[i]
        else:
            res_ = '0' + res_
    return res, int(res_[::-1])

N = 30

for n in range(1,N):
    enc, enc_ = getFibEncoding(n)
    print(n, enc, enc_)

    with open(f'fibofish/data/secret/test_{n}.in', 'w') as f:
        f.write(str(n))
    with open(f'fibofish/data/secret/test_{n}.ans', 'w') as f:
        f.write(str(enc))


import random

for i in range(50):
    n = random.randint(1,int(1e18))
    enc, enc_ = getFibEncoding(n)
    print(n, enc)
    with open(f'fibofish/data/secret/random_all_{n}.in', 'w') as f:
        f.write(str(n))
    with open(f'fibofish/data/secret/random_all_{n}.ans', 'w') as f:
        f.write(str(enc))


for i in range(50):
    n = random.randint(int(1e15),int(1e18))
    enc, enc_ = getFibEncoding(n)
    print(n, enc)
    with open(f'fibofish/data/secret/random_all_{n}.in', 'w') as f:
        f.write(str(n))
    with open(f'fibofish/data/secret/random_all_{n}.ans', 'w') as f:
        f.write(str(enc))

for n in [int(1e18),int(1e18)-1,int(1e18)-2,int(1e18)-3]:
    enc, enc_ = getFibEncoding(n)
    print(n, enc)
    with open(f'fibofish/data/secret/highest_{n}.in', 'w') as f:
        f.write(str(n))
    with open(f'fibofish/data/secret/highest_{n}.ans', 'w') as f:
        f.write(str(enc))