import bisect

nq = input()
nq = nq.split(" ")
n = int(nq[0])
q = int(nq[1])

antennas = input().split(" ")
positions = []
for i in range(q):
	positions.append(int(input()))
for i in range(n):
	antennas[i] = int(antennas[i])
antennas.sort()
for i in range(q):
	index = bisect.bisect_left(antennas, positions[i])
	best = None
	if index < n:
		best = antennas[index]
	
	if index > 0 :
		if best == None:
			best = antennas[index-1]
		else:
			if abs(antennas[index-1] - positions[i]) < abs(best - positions[i]):
				best = antennas[index-1]
    		
	print(best)