import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay

# 1. points in the
points = np.array([
    [3, 5],  # A
    [6, 6],  # B
    [6, 4],  # C
    [9, 5],  # D
    [9, 7]   # E
])

# 2.compute the Delaunay triangulation
tri = Delaunay(points)

# print the Delaunay triangulation info:
# tri.simplices is a (num_triangles x 3) array of indices into "points"
print("Delaunay Triangulation (simplices):")
for simplex in tri.simplices:
    # e.g., [0, 1, 2] means the triangle is formed by points[0], points[1], points[2]
    print("Triangle:", simplex, " => ", points[simplex])

# 3.compute the Voronoi diagram
vor = Voronoi(points)

# print Voronoi regions and vertices info
print("\nVoronoi vertices:\n", vor.vertices)
print("\nVoronoi regions (each is a list of indices into vor.vertices):")
for i, region in enumerate(vor.regions):
    # region can be empty or contain -1 if unbounded
    print(f"Region {i}: {region}")

# 4. Plot everything

fig, ax = plt.subplots(figsize=(6,6))

# 4a. Plot the Delaunay triangulation
# 'triangulation' in matplotlib can be done with the Delaunay object:
plt.triplot(points[:,0], points[:,1], tri.simplices.copy(), color="blue", linestyle="--", label="Delaunay Triangulation")

# 4b. Plot the Voronoi diagram on top
# voronoi_plot_2d is convenient, but we'll pass our existing figure & axes
voronoi_plot_2d(vor, ax=ax, show_points=False, show_vertices=True, line_colors='red', point_size=2)

# 4c. Plot the original points
plt.scatter(points[:,0], points[:,1], color="black", zorder=10)
for i, p in enumerate(points):
    plt.text(p[0] + 0.1, p[1] + 0.1, f"P{i}", fontsize=12)

plt.title("Delaunay Triangulation & Voronoi Diagram")
plt.legend()
plt.axis("equal")
plt.show()
