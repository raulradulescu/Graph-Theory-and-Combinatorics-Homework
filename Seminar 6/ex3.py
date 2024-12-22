import numpy as np
from itertools import combinations

#fixed points
A = np.array([1, 6])
B = np.array([1, 1])
C = np.array([-4, 7])
D = np.array([6, 7])
E = np.array([1, -1])
F = np.array([5, 3])
P = np.array([-2, 3])

def distance(u,v):
    return np.linalg.norm(u - v)

def kruskal_mst_cost(points):
    # points: list of (name, np.array([x,y])) 
    # 1) build all edges
    edges = []
    for (i, (ni, pi)), (j, (nj, pj)) in combinations(enumerate(points), 2):
        edges.append((distance(pi, pj), i, j))
    # 2) sort by length
    edges.sort(key=lambda x: x[0])
    # 3) union-find
    parent = list(range(len(points)))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    mst_cost = 0.0
    for w, i, j in edges:
        ri, rj = find(i), find(j)
        if ri != rj:
            mst_cost += w
            parent[ri] = rj
    return mst_cost

lambdas_to_test = np.linspace(-5, 10, 100)  # example range
best_val = None
best_mst = float('inf')

for lam in lambdas_to_test:
    Q = np.array([lam - 2, 3])
    pts = [
        ("A", A), ("B", B), ("C", C),
        ("D", D), ("E", E), ("F", F),
        ("P", P), ("Q", Q)
    ]
    cost = kruskal_mst_cost(pts)
    if cost < best_mst:
        best_mst = cost
        best_val = lam

print("Best lambda ~", best_val)
print("MST cost ~", best_mst)
