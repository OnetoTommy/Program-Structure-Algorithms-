import matplotlib.pyplot as plt
import numpy as np
import math

#1
# Define the function f(n)
# f(n) = (n^2)*(logn) + n + 3
# Big O notation
def f(n):
    return n**2 * np.log(n) + n + 3

# Generate a range of n values
n = np.arange(1, 1001)

# Calculate values for each term and the entire function
f_values = f(n)
n2_logn_values = n**2 * np.log(n)
n_values = n
constant_values = np.full_like(n, 3)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n, f_values, label='f(n) = n^2 log(n) + n + 3', color='black')
plt.plot(n, n2_logn_values, label='n^2 log(n)', linestyle='--', color='red')
plt.plot(n, n_values, label='n', linestyle='--', color='blue')
plt.plot(n, constant_values, label='3', linestyle='--', color='green')

# Adding labels and legend
plt.xlabel('n')
plt.ylabel('Value')
plt.title('Growth of f(n) and its Components')
plt.legend()
plt.yscale('log') # Logarithmic scale for better visualization
plt.grid(True)
plt.show()
#-----------------------------------------------------------
#2
# f(n) = n! + 100nlogn
# Big O Notation
# Define the functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def f(n):
    return factorial(n) + 100 * n * np.log(n)

def exp_n_n(n):
    return n**n

# Generate a range of n values (keeping it small due to rapid growth)
n = np.arange(1, 11)  # Using numbers from 1 to 10

# Calculate values for each function
f_values = np.array([f(i) for i in n])
factorial_values = np.array([factorial(i) for i in n])
exp_values = np.array([exp_n_n(i) for i in n])

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n, f_values, label='f(n) = n! + 100nlog(n)', color='black')
plt.plot(n, factorial_values, label='n!', linestyle='--', color='red')
plt.plot(n, exp_values, label='n^n', linestyle='--', color='blue')

# Adding labels and legend
plt.xlabel('n')
plt.ylabel('Value')
plt.title('Comparison of Function Growth')
plt.legend()
plt.yscale('log')  # Logarithmic scale for better visualization
plt.grid(True)
plt.show()
#-----------------------------------------
#3
#f(n) = 3n^3 + 5n^2 + 100 + 2^2n
# Big O notation
# Define the function f(n)
def f(n):
    return 3*n**4 + 5*n**2 + 100 + 2**(2*n)

# Generate a range of n values
n = np.arange(1, 15)  # Adjust the range as needed

# Calculate values for each term and the entire function
f_values = f(n)
term1_values = 3*n**4
term2_values = 5*n**2
term3_values = np.full_like(n, 100)
term4_values = 2**(2*n)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(n, f_values, label='f(n) = 3n^4 + 5n^2 + 100 + 2^(2n)', color='black')
plt.plot(n, term1_values, label='3n^4', linestyle='--', color='red')
plt.plot(n, term2_values, label='5n^2', linestyle='--', color='blue')
plt.plot(n, term3_values, label='100', linestyle='--', color='green')
plt.plot(n, term4_values, label='2^(2n)', linestyle='--', color='orange')

# Adding labels and legend
plt.xlabel('n')
plt.ylabel('Value')
plt.title('Growth of f(n) and its Components')
plt.legend()
plt.yscale('log') # Logarithmic scale for better visualization
plt.grid(True)
plt.show()

#--------------------------------------------------------
# 4
# f(n) = 10n^2 +sqrt(n) + log n
# Big O notation
# Define the function f(n)
def f(n):
    return n**2 + np.sqrt(n) + np.log(n)

# Generate a range of n values
n = np.linspace(1, 1000, 1000)

# Compute f(n), n^2, sqrt(n), and log(n) for each value in n
f_n = f(n)
quadratic_n = n**2
sqrt_n = np.sqrt(n)
log_n = np.log(n)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, f_n, label="f(n) = n^2 + sqrt(n) + log(n)")
plt.plot(n, quadratic_n, label="n^2", linestyle="--")
plt.plot(n, sqrt_n, label="sqrt(n)", linestyle=":")
plt.plot(n, log_n, label="log(n)", linestyle="-.")
plt.xlabel("n")
plt.ylabel("Function value")
plt.title("Comparison of f(n) and its components")
plt.legend()
plt.grid(True)
plt.show()
#-----------------------------------------------------

# -- Big Omega 
#1 - Big Omega
#f(n) = n! + n2 +n3
# Define the function f(n)

def f(n):
    return math.factorial(n) + n**2 + n**3

# Generate a range of n values
# We must limit the range because factorials grow extremely fast
n = np.arange(1, 11)  # The range is limited to keep the factorial values within a plot-able range

# Compute f(n), n^2, n^3, and n! for each value in n
f_n = np.array([f(i) for i in n])
squared_n = n**2
cubed_n = n**3
factorial_n = np.array([math.factorial(i) for i in n])

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(n, f_n, label="f(n) = n! + n^2 + n^3")
plt.plot(n, squared_n, label="n^2", linestyle="--")
plt.plot(n, cubed_n, label="n^3", linestyle=":")
plt.plot(n, factorial_n, label="n!", linestyle="-.")
plt.xlabel("n")
plt.ylabel("Function value")
plt.title("Growth of f(n) compared to its components")
plt.legend()
plt.grid(True)
plt.show()


# def f(n):
#     return math.factorial(n) + n**2 + 3*n

# # Generate a range of n values
# n = np.arange(1, 11)  # Using numbers from 1 to 10 for illustration

# # Calculate values for the function and its components
# f_values = np.array([f(i) for i in n])
# factorial_values = np.array([math.factorial(i) for i in n])
# n_squared_values = n**2
# three_n_values = 3 * n

# # Plotting the results
# plt.figure(figsize=(10, 6))
# # plt.plot(n, f_values, label='f(n) = n! + n^2 + 3n', color='black')
# plt.plot(n, factorial_values, label='n!', linestyle='--', color='red')
# plt.plot(n, n_squared_values, label='n^2', linestyle='--', color='blue')
# plt.plot(n, three_n_values, label='3n', linestyle='--', color='green')

# # Adding labels and legend
# plt.xlabel('n')
# plt.ylabel('Value')
# plt.title('Growth of f(n) = n! + n^2 + 3n and its Components')
# plt.legend()
# plt.grid(True)
# plt.show()


#-----------------------------------------

#2 - Big Omega
#f(n) = log n + n + 10
#Big Omega
# Define the function f(n)
def f(n):
    return np.log(n) + n + 10

# Generate a range of n values
n = np.linspace(1, 1000, 1000)  # Avoid starting from 0 to prevent log(0)

# Compute f(n) and n for each value in n
f_n = f(n)
linear_n = n

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, f_n, label="f(n) = log n + n + 10")
plt.plot(n, linear_n, label="n", linestyle="--")
plt.xlabel("n")
plt.ylabel("Function value")
plt.title("Growth of f(n) compared to its dominant term n")
plt.legend()
plt.grid(True)
plt.show()

#----------------------------

# 3 - Big Omega
# Define the function f(n)
def f(n):
    return 2**n + n**3

# Generate a range of n values
n = np.arange(1, 20)  # We keep n small because 2^n grows very fast

# Compute f(n), 2^n, and n^3 for each value in n
f_n = np.array([f(i) for i in n])
exp_n = 2**n
poly_n = n**3

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, f_n, label="f(n) = 2^n + n^3")
plt.plot(n, exp_n, label="2^n", linestyle="--")
plt.plot(n, poly_n, label="n^3", linestyle=":")
plt.xlabel("n")
plt.ylabel("Function value")
plt.title("Growth of f(n) compared to its components")
plt.legend()
plt.grid(True)
plt.show()

#-------------------------------------
# Define the function f(n) = log(n!) using the complete Stirling's approximation
# Big Omega
def f(n):
    return n*np.log(n) - n + 0.5*np.log(2*np.pi*n)

# Generate a range of n values
n = np.arange(1, 1000)

# Compute f(n) and n log(n) for each value in n
f_n = np.array([f(i) for i in n])
n_log_n = n * np.log(n)

# Plotting
plt.figure(figsize=(12, 7))
plt.plot(n, f_n, label="f(n) = log(n!) using Stirling's approximation")
plt.plot(n, n_log_n, label="n log(n)", linestyle="--")
plt.xlabel("n")
plt.ylabel("Function value")
plt.title("Comparison of f(n) and n log(n) using correct Stirling's approximation")
plt.legend()
plt.grid(True)
plt.show()


#----------------------
#5 - Big Omega
# f(n) = sqrt(n) + logn
#Big Omega
# Define the function f(n)
def f(n):
    return np.sqrt(n) + np.log(n)

# Generate a range of n values
n = np.linspace(1, 1000, 1000)  # Avoid starting from 0 to prevent log(0)

# Compute f(n) and sqrt(n) for each value in n
f_n = f(n)
sqrt_n = np.sqrt(n)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n, f_n, label="f(n) = sqrt(n) + log(n)")
plt.plot(n, sqrt_n, label="sqrt(n)", linestyle="--")
plt.xlabel("n")
plt.ylabel("Function value")
plt.title("Comparison of f(n) and sqrt(n)")
plt.legend()
plt.grid(True)
plt.show()


#-----------------------
# # Define the function f(n)
# def f(n):
#     return math.factorial(n) + n**2 + n**3

# # Generate a range of n values
# # We must limit the range because factorials grow extremely fast
# n = np.arange(1, 11)  # The range is limited to keep the factorial values within a plot-able range

# # Compute f(n), n^2, n^3, and n! for each value in n
# f_n = np.array([f(i) for i in n])
# squared_n = n**2
# cubed_n = n**3
# factorial_n = np.array([math.factorial(i) for i in n])

# # Plotting
# plt.figure(figsize=(12, 8))
# plt.plot(n, f_n, label="f(n) = n! + n^2 + n^3")
# plt.plot(n, squared_n, label="n^2", linestyle="--")
# plt.plot(n, cubed_n, label="n^3", linestyle=":")
# plt.plot(n, factorial_n, label="n!", linestyle="-.")
# plt.xlabel("n")
# plt.ylabel("Function value")
# plt.title("Growth of f(n) compared to its components")
# plt.legend()
# plt.grid(True)
# plt.show()

