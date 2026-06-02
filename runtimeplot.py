# Runtime Comparison Plot

plt.figure(figsize=(10,6))

plt.plot(
    sample_sizes,
    basic_runtimes,
    marker='o',
    label='Basic Version'
)

plt.plot(
    sample_sizes,
    optimized_runtimes,
    marker='s',
    label='Optimized Version'
)

plt.xlabel('Number of Samples (N)')
plt.ylabel('Average Runtime (seconds)')

plt.title('Monte Carlo Pi Approximation Runtime Comparison')

plt.legend()

plt.grid(True)

plt.show()
