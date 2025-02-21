import numpy as np
import matplotlib.pyplot as plt

# Create an array of x values
x = np.linspace(1, 30, 400)

# Define the functions, including the new 1/3 power function
functions = {
    r'$\log_2 x$': np.log2(x),
    r'$\sqrt{x}$': np.sqrt(x),
    r'$x^{1/3}$': x ** (1/3),
    r'$x$': x,
    r'$x \log_2 x$': x * np.log2(x),
    r'$x^2$': x ** 2,
    r'$x^3$': x ** 3,
    r'$2^x$': 2 ** x,
    r'$3^x$': 3 ** x,
}

# Plot the functions
plt.figure(figsize=(12, 10))

for label, y in functions.items():
    plt.plot(x, y, label=label)

# Adjust axes limits for better visualization
plt.ylim(0, 100)  # Increased f(x) axis range
plt.xlim(0, 30)

# Add labels and title
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Comparison of Common Complexity Functions with $x^{1/3}$ Added', fontsize=14)

# Add a legend
plt.legend(loc='upper left', fontsize=10)

# Show grid
plt.grid(True)

# Display the plot
plt.show()
