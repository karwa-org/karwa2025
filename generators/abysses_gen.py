import random
import math
from decimal import Decimal, getcontext

# Set desired precision for Decimal arithmetic.
getcontext().prec = 28

TOLERANCE = Decimal("1e-5")  # tolerance for floating-point comparisons

def generate_random_points(n, x_range, y_range, degree_range=(0, 359)):
    points = []
    for _ in range(n):
        # Generate coordinates as Decimals.
        x = Decimal(str(random.uniform(*x_range)))
        y = Decimal(str(random.uniform(*y_range)))
        degree = random.randint(*degree_range)
        points.append((x, y, degree))
    return points

def is_angle_in_direction(p1, p2):
    """
    Check if the angle of point A (p1) is in the direction of point B (p2).
    p1 and p2 are tuples (x, y, degree) where x and y are Decimals and degree is an integer.
    """
    x1, y1, degree1 = p1
    x2, y2, _ = p2
    # Compute differences using Decimal arithmetic.
    dx = x2 - x1
    dy = y2 - y1
    # For trigonometry, convert to float.
    angle_to_b = math.degrees(math.atan2(float(dy), float(dx))) % 360
    # Compare computed angle with stored degree (converted to Decimal) within tolerance.
    return abs(Decimal(angle_to_b) - Decimal(degree1)) < TOLERANCE

def generate_points_with_chain(n, x_range, y_range, k):
    """
    Generate n points ensuring that the first k points form a chain.
    For the chain, each point's angle is set exactly to point to the next point,
    and stored as an integer. All coordinates are stored as Decimals.
    Raises a ValueError if k > n.
    """
    if k > n:
        raise ValueError("k must be less than or equal to n")
    
    points_chain = []
    
    # Start the chain near the center of the provided range.
    mid_x = Decimal(x_range[0] + x_range[1]) / 2
    mid_y = Decimal(y_range[0] + y_range[1]) / 2
    quarter_x = Decimal(x_range[1] - x_range[0]) / 4
    quarter_y = Decimal(y_range[1] - y_range[0]) / 4
    p0_x = Decimal(str(random.uniform(float(mid_x - quarter_x), float(mid_x + quarter_x))))
    p0_y = Decimal(str(random.uniform(float(mid_y - quarter_y), float(mid_y + quarter_y))))
    # Temporary degree (will be updated when linking to p1)
    p0 = (p0_x, p0_y, 0)
    points_chain.append(p0)
    
    current = p0
    # Build chain so that chain length equals exactly k.
    for i in range(1, k):
        # Pick a random angle (in degrees) for the chain link.
        chosen_angle = random.randint(0, 359)
        # Choose a distance such that the next point stays within bounds.
        d_min = Decimal("1")
        d_max = Decimal(min(x_range[1] - x_range[0], y_range[1] - y_range[0])) / 10
        d = Decimal(str(random.uniform(float(d_min), float(d_max))))
        rad = math.radians(chosen_angle)
        # Calculate next point's coordinates using float then convert to Decimal.
        next_x = current[0] + d * Decimal(math.cos(rad))
        next_y = current[1] + d * Decimal(math.sin(rad))
        # Clamp to allowed ranges.
        next_x = max(Decimal(x_range[0]), min(next_x, Decimal(x_range[1])))
        next_y = max(Decimal(y_range[0]), min(next_y, Decimal(y_range[1])))
        # Compute the actual angle from current to next point (using float conversion) and store it as an integer.
        actual_angle = int(round(math.degrees(math.atan2(float(next_y - current[1]), float(next_x - current[0]))))) % 360
        # Update current point's degree so that it points exactly to the next point.
        current = (current[0], current[1], actual_angle)
        # Replace the last point in the chain with the updated version.
        points_chain[-1] = current
        # Create the next point with a temporary degree 0 (to be updated if there are further chain links).
        next_point = (next_x, next_y, 0)
        points_chain.append(next_point)
        current = next_point
    
    # For the last point in the chain, assign a random degree.
    last_point = points_chain[-1]
    last_point = (last_point[0], last_point[1], random.randint(0, 359))
    points_chain[-1] = last_point
    
    print("Chain length:", len(points_chain), "Expected:", k)
    assert(len(points_chain) == k)
    
    # Generate the remaining n - k points randomly.
    remaining_points = generate_random_points(n - k, x_range, y_range)
    
    # Combine the chain with the remaining random points.
    return points_chain + remaining_points

def build_adjacency_list(points):
    n = len(points)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if is_angle_in_direction(points[i], points[j]):
                adj[i].append(j)
    return adj

def dfs(node, visited, adj):
    """
    Depth-first search to compute the size of a component starting from node.
    """
    if visited[node]:
        return 0
    visited[node] = True
    size = 1
    for neighbor in adj[node]:
        size += dfs(neighbor, visited, adj)
    return size

def find_component_size_for_point(index, adj):
    n = len(adj)
    visited = [False] * n
    return dfs(index, visited, adj)


def solve(n, fishes, index_query):
    in_group = [False] * n
    in_group[index_query], found, target, size = True, True, fishes[index_query], 1
    while found:
        i = find_first_intersection(fishes, *target)
        if i == -1 or in_group[i]:
            found = False
        else:
            in_group[i], size, target = True, size+1, fishes[i]
    return size

def find_first_intersection(points, x0, y0, angle):
    angle_rad = math.radians(angle)
    dx, dy = Decimal(math.cos(angle_rad)), Decimal(math.sin(angle_rad))
    index_closest, best_dist_squared = -1, float('inf')
    for i in range(len(points)):
        x,y,a = points[i]
        if abs(x-x0) <= TOLERANCE and abs(y-y0) <= TOLERANCE: continue # same point
        dist = dx*(y-y0) - dy*(x-x0) # dist between (x,y) and the beam
        if abs(dist) <= TOLERANCE and (x-x0)*dx >= 0 and (y-y0)*dy >= 0:
            dist_squared = (x-x0)**2 + (y-y0)**2 # dist between (x,y) and (x0,y0)
            if dist_squared < best_dist_squared:
                best_dist_squared, closest_point, index_closest = dist_squared, (x,y,a), i
    return index_closest


# Generate several test cases.
for idx in range(10,15):
    # Example usage:
    n = 1000             # Total number of points
    x_range = (0, 10000000)
    y_range = (0, 10000000)
    k = random.randint(100,n)  # We want a chain (component) of size exactly k

    points = generate_points_with_chain(n, x_range, y_range, k)
    starting_fish = points[0]
    random.shuffle(points)
    starting_idx = points.index(starting_fish)
    adj = build_adjacency_list(points)

    # Check the chain by computing the component size for each chain point.
    print("Chain component sizes:")
    for i in range(k):
        comp_size = find_component_size_for_point(i, adj)
        print(f"Component size starting at chain point {i}: {comp_size}")

    print("\nAll Points:")
    for i, p in enumerate(points):
        print(f"{i}: {p}")

    print("\nAdjacency list:")
    for i, neighbors in enumerate(adj):
        print(f"{i}: {neighbors}")

    # Compute answer (component size starting at point 0) using DFS.
    visited = [False] * n
    ans = dfs(starting_idx, visited, adj)
    ans2 = solve(n, points, starting_idx)
    if ans != ans2:
        print("not same answer...", ans, ans2)
    assert(len(points) == n)

    # Write test case to file.
    with open(f"random-medium-{idx+1}.in", "w") as file:
        file.write(f"{n}\n")
        for p in points:
            # Write Decimal values as strings.
            file.write(f"{p[0]} {p[1]} {p[2]}\n")
        file.write(f"{starting_idx}\n")
    with open(f"random-medium-{idx+1}.ans", "w") as file:
        file.write(f"{ans2}\n")
