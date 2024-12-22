import numpy as np
from scipy.spatial import Delaunay

A = np.array([1, -1])
B = np.array([-1, 1])
C = np.array([2, -1])
D = np.array([1, 1])
E = np.array([0, 2])

def triangulation_info(lmbd):
    M = np.array([1, lmbd])
    pts = np.vstack([A, B, C, D, E, M])
    tri = Delaunay(pts)
    # tri.simplices is an array of shape (num_triangles, 3)
    num_triangles = len(tri.simplices)
    # to count edges in the triangulation, note each simplex has 3 edges,
    # but edges can be shared. We can collect them in a set:
    edges_set = set()
    for simplex in tri.simplices:
        s = sorted(simplex)
        # all 3 edges
        edges_set.add((s[0], s[1]))
        edges_set.add((s[1], s[2]))
        edges_set.add((s[0], s[2]))
    num_edges = len(edges_set)
    return num_triangles, num_edges

# example usage:
for lam in [-2, 0, 0.5, 2, 10]:
    t, e = triangulation_info(lam)
    print(f"lambda is {lam}, number of triangles is {t}, number of edges is{e}")
