# Live Convergence Visualisation

import numpy as np
import matplotlib.pyplot as plt

# parameters
TOTAL_POINTS = 1_000_000
BATCH_SIZE = 5000
SEED = 42

# random seed
np.random.seed(SEED)

# storage variables
inside_circle = 0
sample_counts = []
pi_estimates = []
errors = []

#plot setup
plt.ion()
fig, ax = plt.subplots(figsize=(10,6))
line_estimate, = ax.plot([], [], label='Estimated π')
line_true = ax.axhline(
 np.pi,
 color='red',
 linestyle='--',
 label=f'True π = {np.pi:.6f}'
)
ax.set_xlabel('Number of Samples')
ax.set_ylabel('π Estimate')
ax.set_title('Monte Carlo π Convergence')
ax.legend()

# monte carlo simulation
for current_N in range(BATCH_SIZE,
 TOTAL_POINTS + 1,
 BATCH_SIZE):
  # Generate batch of random points
 x = np.random.uniform(-1, 1, BATCH_SIZE)
 y = np.random.uniform(-1, 1, BATCH_SIZE)
 # Count points inside circle
 inside_circle += np.sum(x**2 + y**2 <= 1)
 # Compute approximation
 approx_pi = 4 * inside_circle / current_N
 # Relative percentage error
 error = (
 100 * abs(approx_pi - np.pi) / np.pi
 )
 # Store values
 sample_counts.append(current_N)
 pi_estimates.append(approx_pi)
 errors.append(error)
 # Console monitoring
 print(
 f"N = {current_N:<10}"
 f"Approx π = {approx_pi:.8f} "
 f"Error = {error:.6f}%",
 end='\r'
 )
 # Update graph
 line_estimate.set_data(
 sample_counts,
 pi_estimates
 )
 ax.relim()
 ax.autoscale_view()
 plt.pause(0.01)

# final display
plt.ioff()
plt.show()
