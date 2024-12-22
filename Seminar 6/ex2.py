import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

points = np.array([
    [5, 1],   # A1
    [7, -1],  # A2
    [9, -1],  # A3
    [7,  3],  # A4
    [11,1],   # A5
    [9,  3],  # A6
    [4,  5],  # A7
    [12, -3], # A8
])

vor = Voronoi(points)

fig = voronoi_plot_2d(vor)
plt.scatter(points[:,0], points[:,1], c='red')
plt.show()

# Then inspect vor.ridge_vertices, vor.vertices, etc. to count unbounded edges
