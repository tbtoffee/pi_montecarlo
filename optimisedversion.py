# improved cde using numpy vectorisation

import numpy as np
import time

def estimate_pi_vectorized(num_points, seed=42):

    np.random.seed(seed)

    start_time = time.time()

    x = np.random.uniform(-1, 1, num_points)
    y = np.random.uniform(-1, 1, num_points)

    distances = x**2 + y**2

    inside_circle = np.sum(distances <= 1)

    pi_estimate = 4 * inside_circle / num_points

    runtime = time.time() - start_time

    return pi_estimate, runtime

num_points = 10_000_000

estimate, runtime = estimate_pi_vectorized(num_points)

print(f"Estimated pi: {estimate}")
print(f"Runtime: {runtime:.4f} seconds")