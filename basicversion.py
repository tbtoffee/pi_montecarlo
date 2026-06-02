# initial basic implementation

import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance_squared = x**2 + y**2

        if distance_squared <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

if __name__ == '__main__':
    num_points = 100000
    
    estimated_pi = estimate_pi(num_points)
    
    print(f"Estimated π: {estimated_pi}")
