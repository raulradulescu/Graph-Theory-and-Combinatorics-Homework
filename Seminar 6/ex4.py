import numpy as np
from scipy.spatial import ConvexHull

A = [(1+i, i-1) for i in range(6)]
B = [(-i, i)   for i in range(6)]
C = [(0, i)    for i in range(6)]
all_points = np.array(A + B + C)

hull = ConvexHull(all_points)
num_hull_edges = len(hull.simplices)  # each simplex is an edge in 2D
print("Number of half-line Voronoi edges =", num_hull_edges)
