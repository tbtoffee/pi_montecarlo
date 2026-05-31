# Visualisation Component

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

num_points = 5000

x = np.random.uniform(-1,1,num_points)
y = np.random.uniform(-1,1,num_points)

inside = x**2 + y**2 <= 1

plt.figure(figsize=(8,8))

plt.scatter(x[inside], y[inside], s=5)
plt.scatter(x[~inside], y[~inside], s=5)

circle = plt.Circle((0,0), 1, fill=False)

plt.gca().add_patch(circle)

plt.xlim([-1,1])
plt.ylim([-1,1])

plt.gca().set_aspect('equal')

plt.legend()

plt.show()
