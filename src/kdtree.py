class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

def build_kdtree(points, depth=0):
    try:
        k = len(points[0])
    except IndexError:
        return None

    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return KDNode(
        point=points[median],
        axis=axis,
        left=build_kdtree(points[:median], depth + 1),
        right=build_kdtree(points[median + 1:], depth + 1)
    )

def distance(p1, p2):
    return sum((i-j)**2 for i, j in zip(p1, p2))**0.5

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


def queryByRadius(node, point, radius):
    """
    Find all points in the KDTree within a given radius of a point.

    Args:
    - node (KDNode): the root node of the KDTree to search
    - point (tuple): the point around which to search for neighbors
    - radius (float): the search radius

    Returns:
    - neighbors (list): a list of all points within the search radius
    """
    if node is None:
        return []

    if node.left is None and node.right is None:
        if distance(node.point, point) <= radius:
            return [node.point]
        else:
            return []

    if node.axis == 0:
        axis_distance = abs(node.point[0] - point[0])
    else:
        axis_distance = abs(node.point[1] - point[1])

    if axis_distance <= radius and node.point != point:
        neighbors = [node.point]
    else:
        neighbors = []

    if node.left is not None and point[node.axis] - radius <= node.point[node.axis]:
        neighbors += queryByRadius(node.left, point, radius)

    if node.right is not None and point[node.axis] + radius >= node.point[node.axis]:
        neighbors += queryByRadius(node.right, point, radius)

    return neighbors

P = [(1,2), (3,4), (5,6), (7,8), (9, 10)]
# P =  [(1, 2), (3, 2), (4, 1), (3, 5), (5,6)]
radius = 3
printDistances(P, radius, single=(5,6))
# neighbors = find_high_density_points(P,3,2)
tree = build_kdtree(P)
neighbors = queryByRadius(tree, (5,6), radius)
print(neighbors)
