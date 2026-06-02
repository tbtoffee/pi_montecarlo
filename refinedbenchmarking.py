# Refined benchmarking script

import time
import numpy as np
import matplotlib.pyplot as plt

from basicversion import estimate_pi
from optimisedversion import estimate_pi_vectorized

# parameters
sample_sizes = [
    10_000,
    100_000,
    1_000_000,
    5_000_000,
    10_000_000
]

num_trials = 5


# storage
basic_runtimes = []
optimized_runtimes = []

# basic version
print("\nBenchmarking Basic Version")

for N in sample_sizes:

    trial_times = []

    for _ in range(num_trials):

        start = time.perf_counter()

        estimate_pi(N)

        end = time.perf_counter()

        trial_times.append(end - start)

    average_time = np.mean(trial_times)

    basic_runtimes.append(average_time)

    print(
        f"N = {N:<10}"
        f" Average Runtime = {average_time:.6f} s"
    )

# optimised version
print("\nBenchmarking Optimized Version")

for N in sample_sizes:

    trial_times = []

    for _ in range(num_trials):

        _, runtime = estimate_pi_vectorized(N)

        trial_times.append(runtime)

    average_time = np.mean(trial_times)

    optimized_runtimes.append(average_time)

    print(
        f"N = {N:<10}"
        f" Average Runtime = {average_time:.6f} s"
    )
