# This code calculates the variance and standard deviation of a given dataset.
# It defines two functions: variance and standard_deviation.
# The variance function computes the average of the squared differences from the mean,
# while the standard_deviation function returns the square root of the variance.
import statistics

data = [70, 75, 80, 85, 90]
def variance(data):
    if not data:
        return 0
    return statistics.variance(data)

def standard_deviation(data):
    if not data:
        return 0
    return statistics.stdev(data)

print("Data:", data)
var = variance(data)
std_dev = standard_deviation(data)
print("Variance:", var)
print("Standard Deviation:", std_dev)
