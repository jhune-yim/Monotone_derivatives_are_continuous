import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# 1. Define the function and its analytical derivative
def f(x):
    """Example function: f(x) = x^3 - 2x + 1"""
    return x**3 - 2*x + 1

def f_prime(x):
    """Derivative: f'(x) = 3x^2 - 2"""
    return 3*x**2 - 2

# 2. Define the closed interval [a, b]
a, b = -2, 2

# Calculate the slope of the secant line between a and b
secant_slope = (f(b) - f(a)) / (b - a)

# 3. Define the objective function to find c
def target_equation(x):
    """We want to find x where f'(x) - secant_slope == 0"""
    return f_prime(x) - secant_slope

# 4. Solve for c
# The MVT guarantees at least one root in (a, b).
# We use the midpoint as our initial guess for the numerical solver.
initial_guess = (a + b) / 2.0
c = fsolve(target_equation, x0=initial_guess)[0]

print(f"Interval: [{a}, {b}]")
print(f"Secant line slope: {secant_slope:.4f}")
print(f"Point c found at: {c:.4f}")
print(f"f'(c) value: {f_prime(c):.4f}")

# 5. Visualization
x_vals = np.linspace(a - 0.5, b + 0.5, 400)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="f(x) = x³ - 2x + 1", color="blue")

# Plot secant line
secant_line = f(a) + secant_slope * (x_vals - a)
plt.plot(x_vals, secant_line, '--', color="gray", label="Secant Line")
plt.scatter([a, b], [f(a), f(b)], color="black", zorder=5) # Endpoints

# Plot tangent line at c
tangent_line = f(c) + f_prime(c) * (x_vals - c)
plt.plot(x_vals, tangent_line, '-.', color="red", label=f"Tangent at c ≈ {c:.2f}")
plt.scatter([c], [f(c)], color="red", zorder=5) # The point c

plt.title("Mean Value Theorem")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
