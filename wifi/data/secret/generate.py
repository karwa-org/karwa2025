import random
import collections
import os

def generate_sample(path, upper_n, upper_q, n_sample=10, random_param=False, start_index=1):
    for i in range(start_index, start_index + n_sample):
        with open(path + f"{i}.in", "w") as file:
            if random_param:
                n = random.randint(1, upper_n + 1)
                q = random.randint(1, upper_q + 1)
            else:
                n = upper_n
                q = upper_q

            file.write(f"{n} {q}\n")

            visited = collections.defaultdict(bool)
            cnt = 0
            while cnt < n:
                v = random.randint(0, int(1e18) + 1)
                if visited[v]:
                    continue
                if cnt == n-1:
                    file.write(f"{v}")
                else:
                    file.write(f"{v} ")
                cnt += 1

            file.write("\n")
            for _ in range(q):
                v = random.randint(0, int(1e18) + 1)
                file.write(f"{v}\n")

generate_sample("group1/", 1000,   1000,    n_sample=5,  random_param=True)
generate_sample("group1/", 10,     10,      n_sample=5,  random_param=True,start_index=6)
generate_sample("group2/", 10000,  10000,                random_param=True)
generate_sample("group3/", 200000, 200000,               random_param=True)

generate_sample("group1/", 1000,   1000,    n_sample=1, start_index=11)
generate_sample("group2/", 10000,  10000,   n_sample=1, start_index=11)
generate_sample("group3/", 100000, 100000,  n_sample=1, start_index=11)

