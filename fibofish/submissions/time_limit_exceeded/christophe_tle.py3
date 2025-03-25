N = int(input())

def fibo(n):
    if n == 1: return 1
    if n == 2: return 2
    return fibo(n-1) + fibo(n-2)

highest = 2
fiblist = [1,2]
idx = 3
while highest <= N:
    highest = fibo(idx)
    fiblist.append(highest)
    idx += 1


ans, rest = 0, N
for i in range(len(fiblist)-1,-1,-1):
    if fiblist[i] <= rest: ans, rest = ans+i+1, rest-fiblist[i]
print(ans)