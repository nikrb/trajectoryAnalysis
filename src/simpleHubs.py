import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def printDistances(points, radius, single=None):
    if single == None:
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = distance(points[i], points[j])
                if dist <= radius:
                    print(f"Distance between {points[i]} and {points[j]}: {dist:.2f}")
    else:
        for j in range(len(points)):
            if points[j] != single:
                dist = distance(single, points[j])
                if dist <= radius:
                    print(f"Distance between {single} and {points[j]}: {dist:.2f}")


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
# P = [(30,40), (5,25), (10,12), (70,70), (50,30), (35,45)]
# r = 25
# k = 2
# printDistances(P, r, single=(10,12))
P = [(1, 2), (3, 2), (4, 1), (3, 5), (6, 7), (8, 7), (8, 9), (10, 10), (11, 9), (12, 10)]
r = 3
k = 3

H = hubs(P, r, k)

print(H)