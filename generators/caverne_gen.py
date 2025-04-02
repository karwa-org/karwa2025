import random as r

MIN, MAX = 800, 1000

def write(h, l, p, ceil, floor, name):
    print("generating", name)
    f = open(f'{name}.in', "w")
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
    f = open(f'{name}.ans', "w")
    f.write(str(vol - cobble) + '\n')
    f.close()

for a in range(10, 15):
    h = 1000
    l = 1000
    p = 1000
    if a == 0:
        ceil = [[0 for i in range(p)] for j in range(l)]
        floor = [[0 for i in range(p)] for j in range(l)]
    elif a == 1:
        ceil = [[h for i in range(p)] for j in range(l)]
        floor = [[h for i in range(p)] for j in range(l)]
    else:
        ceil = [[r.randint(0, h) for i in range(p)] for j in range(l)]
        floor = [[r.randint(0, h) for i in range(p)] for j in range(l)]
    write(h, l, p, ceil, floor, f"random_max_{a}")