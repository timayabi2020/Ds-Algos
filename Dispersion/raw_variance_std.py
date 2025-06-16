# This code calculates the variance and standard deviation of a given dataset.
# It defines two functions: variance and standard_deviation.
# The variance function computes the average of the squared differences from the mean,
# while the standard_deviation function returns the square root of the variance.
# The main function prints the data, variance, and standard deviation.
data = [70, 75, 80, 85, 90]

def variance(data):
    n = len(data)
    if n == 0:
        return 0
    mean = sum(data) / n
    return sum((x - mean) ** 2 for x in data) / n

def standard_deviation(data):
    return variance(data) ** 0.5


print("Data:", data)
var = variance(data)
std_dev = standard_deviation(data)
print("Variance:", var)
print("Standard Deviation:", std_dev)





