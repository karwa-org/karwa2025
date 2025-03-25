import random as r

for a in range(5):
    h = r.randint(1, 10**3)
    l = r.randint(1, 10**3)
    p = r.randint(1, 10**3)
    print(h, l, p)
    ceil, floor = [[0 for i in range(p)] for j in range(l)], [[0 for i in range(p)] for j in range(l)]
    print("generating", a)
    for i in range(l):
        for j in range(p):
            ceil[i][j] = r.randint(0, h)
            floor[i][j] = r.randint(0, h)
    f = open(f'{a+3}.in', "w")
    f.write(f'{h} {l} {p}\n')
    for m in range(l):
        f.write(" ".join(list(map(str, ceil[m]))) + '\n')
    for m in range(l):
        f.write(" ".join(list(map(str, floor[m]))) + '\n')
    f.close()    


    vol = h*l*p
    cobble = 0

    for i in range(l):
        for j in range(p):
            cobble += min(h, ceil[i][j]+floor[i][j])
    f = open(f'{a+3}.ans', "w")
    f.write(str(vol - cobble))


