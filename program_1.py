import numpy as np
import matplotlib.pyplot as plt

def simple_linear_regression(X, y):
    # Calculate the mean of X and y
    mean_X = np.mean(X)
    mean_y = np.mean(y)
    # Calculate the slope (m) and y-intercept (b) using the least squares method
    numerator = np.sum((X - mean_X) * (y - mean_y))
    denominator = np.sum((X - mean_X) ** 2)
    slope = numerator / denominator
    intercept = mean_y - slope * mean_X
    return slope, intercept


def plot_regression_line(X, y, slope, intercept):
    plt.scatter(X, y, color='blue', label='Data Points')  
    plt.plot(X, slope * X + intercept, color='red', label='Regression Line')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.show()

# # Data
# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
# # Estimate coefficients
# coefficients = simple_linear_regression(x, y)
# print("Estimated coefficients:", coefficients)
# # Plot regression line
# plot_regression_line(x, y, coefficients[0],coefficients[1])

# # Generate some random data
np.random.seed(42)
X = np.random.rand(100, 1) * 10 # Random values for X
y = 3 * X + 2 + np.random.randn(100, 1) * 2 # Linear relationship with noise
slope, intercept = simple_linear_regression(X, y)
print("Slope:", slope)
print("Intercept:", intercept)
plot_regression_line(X, y, slope, intercept)