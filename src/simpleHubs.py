import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# point is x,y tuple, points a list, r radius
def density(point, points, r):
    # Computes the density of a given point in P.
    # The density is defined as the number of points within
    # a distance r of the given point.
    count = 0
    for p in points:
        if math.sqrt((point[0]-p[0])**2 + (point[1]-p[1])**2) <= r:
            count += 1
    return count

def normalize(densities):
    # Normalizes the densities by dividing them by the maximum density.
    max_density = max(densities)
    nd = []
    return [(d[0]/max_density[0], d[1]) for d in densities]

def hubs(P, r, k):
    densities = [(density(p, P, r), p) for p in P]
    densities.sort(reverse=True)
    high_density_points = []
    for d, p in densities:
        if all(distance(p, q[0]) >= r for q in high_density_points):
            high_density_points.append((p,d))
            if len(high_density_points) == k:
                break
    return high_density_points


# P = [(1,2), (3,4), (5,6), (7,8), (9, 10)]
P = [(30,40), (5,25), (10,12), (70,70), (50,30), (35,45)]
r = 25
k = 2

H = hubs(P, r, k)

print(H)