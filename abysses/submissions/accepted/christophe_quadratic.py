import math
def find_first_intersection(points, x0, y0, angle, eps=1e-5):
    angle_rad = math.radians(angle)
    dx, dy = math.cos(angle_rad), math.sin(angle_rad)
    index_closest, best_dist_squared = -1, float('inf')
    for i in range(len(points)):
        x,y,a = points[i]
        if abs(x-x0) <= eps and abs(y-y0) <= eps: continue # same point
        dist = dx*(y-y0) - dy*(x-x0) # dist between (x,y) and the beam
        if abs(dist) <= eps and (x-x0)*dx >= 0 and (y-y0)*dy >= 0:
            dist_squared = (x-x0)**2 + (y-y0)**2 # dist between (x,y) and (x0,y0)
            if dist_squared < best_dist_squared:
                best_dist_squared, closest_point, index_closest = dist_squared, (x,y,a), i
    return index_closest
n = int(input())
fishes = []
for _ in range(n):
    p1, p2, angle = input().split()
    fishes.append((float(p1), float(p2), int(angle)))
index_query = int(input())
in_group = [False] * n
in_group[index_query], found, target, size = True, True, fishes[index_query], 1
while found:
    i = find_first_intersection(fishes, *target)
    if i == -1 or in_group[i]:
        found = False
    else:
        in_group[i], size, target = True, size+1, fishes[i]
print(size)