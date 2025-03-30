import math

def find_first_intersection(points, x0, y0, angle, eps=1e-6):
    angle_rad = math.radians(angle + 90) # axis rotation of 90°
    dx, dy = math.cos(angle_rad), math.sin(angle_rad)

    #print(f" >> debug : angle={angle_rad} : dx={dx} ; dy={dy}")

    closest_point, index_closest, best_t = None, -1, (float('inf'), float('inf'))
    for i in range(len(points)):
        x,y,a = points[i]
        if (x, y) == (x0, y0): continue # should not happen

        # find t such that (x0 + t*dx, y0 + t*dy) = (x,y)
        t_x = (x - x0) / dx if abs(dx) > eps else float('inf')
        t_y = (y - y0) / dy if abs(dy) > eps else float('inf')

        #print(f"   > {x}, {y} : tx={t_x}, ty={t_y}, dist = {abs(t_x - t_y)}")

        dist = abs(t_x - t_y)
        if dist < eps and t_x >= 0 and t_y >= 0: # check for small distance and toward the right direction
            if t_x < best_t[0] or t_y < best_t[1]:
                best_t, closest_point, index_closest = (t_x,t_y), (x,y,a), i

    return closest_point, index_closest

n = int(input())
fishes = []
for _ in range(n):
    p1, p2, angle = input().split()
    fishes.append((float(p1), float(p2), int(angle)))
index_query = int(input())

target, size = fishes.pop(index_query), 1
#grouped = [target]

found = True
while found:
    result, i = find_first_intersection(fishes, *target)
    #print(f"Starting from {target} to {fishes} : found idx {i} = {result}")
    if result is None:
        found = False
    else:
        target = fishes.pop(i)
        size += 1
        #grouped.append(target)
print(size)