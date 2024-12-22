import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

M1 = np.array([
    [0, 1],
    [2, 3],
    [4, 5],
    [10, 6],
    [8, 4],
    [8, 2]
])
M2 = np.array([
    [-4, 2],
    [-4, 6],
    [-6, 2],
    [-2, 6],
    [-8, 4],
    [-6, 6],
    [-8, 2]
])


tri1 = Delaunay(M1)
tri2 = Delaunay(M2)


def count_delaunay_edges(delaunay_obj):
    """
    Count unique edges in a Delaunay triangulation (no duplicates, undirected).
    """
    edges_set = set()
    for simplex in delaunay_obj.simplices:
        # Each simplex is a triangle with 3 vertices => 3 edges
        for i in range(3):
            for j in range(i+1, 3):
                # Sort each edge by vertex index so that (2,5) == (5,2)
                edge = tuple(sorted([simplex[i], simplex[j]]))
                edges_set.add(edge)
    return len(edges_set)

edges1 = count_delaunay_edges(tri1)
edges2 = count_delaunay_edges(tri2)

def count_half_lines(vor):
    """
    Count how many Voronoi edges (ridges) are unbounded (i.e., contain -1 in ridge_vertices).
    """
    count = 0
    for ridge in vor.ridge_vertices:
        if -1 in ridge:  # -1 => unbounded side
            count += 1
    return count

vor1 = Voronoi(M1)
vor2 = Voronoi(M2)

half_lines1 = count_half_lines(vor1)
half_lines2 = count_half_lines(vor2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# --- Plot for M1 ---
ax1.set_title("M1: Triangulation & Voronoi")
ax1.triplot(M1[:,0], M1[:,1], tri1.simplices, color='blue', linestyle='--')
ax1.plot(M1[:,0], M1[:,1], 'ro', label="Points M1")

voronoi_plot_2d(vor1, ax=ax1, show_vertices=False, line_colors='orange', line_width=1)
ax1.legend()
ax1.set_aspect("equal", "box")

ax2.set_title("M2: Triangulation & Voronoi")
ax2.triplot(M2[:,0], M2[:,1], tri2.simplices, color='green', linestyle='--')
ax2.plot(M2[:,0], M2[:,1], 'bo', label="Points M2")

voronoi_plot_2d(vor2, ax=ax2, show_vertices=False, line_colors='purple', line_width=1)
ax2.legend()
ax2.set_aspect("equal", "box")

plt.tight_layout()
plt.show()

print("------------------------------------------------------")
print("Results for M1:")
print(f"  Number of points in M1: {len(M1)}")
print(f"  Number of triangles in the Delaunay triangulation: {len(tri1.simplices)}")
print(f"  Number of edges in the triangulation: {edges1}")
print(f"  Number of half-line edges in the Voronoi diagram: {half_lines1}")

print("\nResults for M2:")
print(f"  Number of points in M2: {len(M2)}")
print(f"  Number of triangles in the Delaunay triangulation: {len(tri2.simplices)}")
print(f"  Number of edges in the triangulation: {edges2}")
print(f"  Number of half-line edges in the Voronoi diagram: {half_lines2}")
print("------------------------------------------------------")
