import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
lambda_rate = 15  # Average number of customers per hour
num_hours = 1000  # Number of hours to simulate

# Generate Poisson-distributed data
customer_arrivals = np.random.poisson(lambda_rate, num_hours)

# Create the main figure
fig, ax = plt.subplots(figsize=(12, 8))

# Plot histogram
ax.hist(customer_arrivals, bins=range(min(customer_arrivals), max(customer_arrivals) + 2, 1),
        density=True, alpha=0.7, color='skyblue', edgecolor='black')

# Plot Poisson PMF
x = np.arange(0, max(customer_arrivals) + 1)
pmf = poisson.pmf(x, lambda_rate)
ax.plot(x, pmf, 'r-', lw=2, label='Poisson PMF')

# Customize the plot
ax.set_title("Poisson Distribution: Coffee Shop Customer Arrivals", fontsize=16)
ax.set_xlabel("Number of Customers per Hour", fontsize=12)
ax.set_ylabel("Probability", fontsize=12)

# Move the legend to the upper left corner
ax.legend(fontsize=10, loc='upper left')

# Add formula, positioned at top right
formula = r"$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$"
ax.text(0.95, 0.95, formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add example calculation, positioned below the formula
example = (f"Example: P(X = 15) with λ = 15\n"
           f"P(X = 15) = {poisson.pmf(15, lambda_rate):.4f}")
ax.text(0.95, 0.82, example, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Add parameters, positioned at the top left corner
params = f"λ (lambda) = {lambda_rate}\nNumber of simulations: {num_hours}"
ax.text(0.05, 0.82, params, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.grid(True)
plt.tight_layout()
plt.show()
