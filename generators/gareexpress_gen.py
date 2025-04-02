import math, random

def ans(N,X):
    return math.ceil(N/X) * X

for i in range(25):
    N = random.randint(0, int(1e9))
    X = random.randint(1, int(1e9))
    with open(f"gareexpress/data/secret/random_{i}.in","w") as f:
        f.write(f"{N}\n{X}\n")
    with open(f"gareexpress/data/secret/random_{i}.ans","w") as f:
        f.write(f"{ans(N,X)}\n")