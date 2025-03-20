import random

for i in range(1, 20, 1):
    with open(f"{i}.in", "w") as file:
        file.write(f"{random.randint(1, 10**9)}\n")
