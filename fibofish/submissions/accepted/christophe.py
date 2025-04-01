N, fiblist = int(input()), [1,2] # N <= 1e18
while fiblist[-1] + fiblist[-2] <= N: fiblist.append(fiblist[-1] + fiblist[-2]) # log(1e18, 1.61803) <= 86.13, so length 85 maximum
ans, rest = 0, N
for i in range(len(fiblist)-1,-1,-1):
    if fiblist[i] <= rest: ans, rest = ans+i+1, rest-fiblist[i]
print(ans)