from methods import *
from test import *
import matplotlib.pyplot as plt
import numpy as np


sigma = 0.1
c = np.array([1,1,1])
r = 1
n = 300
points = sample(n, c, r, sigma)
center, radius = sphereFit(points)

ax = plt.axes(projection = '3d')
plt.plot(points[:, 0], points[:, 1], points[:, 2], 'go')

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = center[0]+np.cos(u)*np.sin(v)
y = center[1]+np.sin(u)*np.sin(v)
z = center[2]+np.cos(v)
ax.plot_wireframe(x, y, z, color="red")

plt.show()
