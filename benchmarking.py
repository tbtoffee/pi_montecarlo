# benchmarking script

import time

from basicversion import estimate_pi
from optimisedversion import estimate_pi_vectorized

sample_sizes = [1000, 10000, 100000, 1000000]

print("Basic Version:")

for n in sample_sizes:

    start = time.time()

    estimate_pi(n)

    runtime = time.time() - start

    print(n, runtime)

print("Optimised Version:")

for n in sample_sizes:

    _, runtime = estimate_pi_vectorized(n)

    print(n, runtime)
