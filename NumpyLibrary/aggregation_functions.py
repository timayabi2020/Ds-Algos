import numpy as np
#Sum of all elements in an array
def sum_array_elements(array):
    """
    Calculate the sum of all elements in a numpy array.
    
    Parameters:
    array (np.ndarray): Input array.
    
    Returns:
    float: Sum of all elements in the array.
    """
    return np.sum(array)

#Mean of all elements in an array
def mean_array_elements(array):
    """
    Calculate the mean of all elements in a numpy array.
    
    Parameters:
    array (np.ndarray): Input array.
    
    Returns:
    float: Mean of all elements in the array.
    """
    return np.mean(array)

#Median of all elements in an array
def median_array_elements(array):
    """
    Calculate the median of all elements in a numpy array.
    
    Parameters:
    array (np.ndarray): Input array.
    
    Returns:
    float: Median of all elements in the array.
    """
    return np.median(array)

#Standard deviation of all elements in an array
def std_array_elements(array):
    """
    Calculate the standard deviation of all elements in a numpy array.
    
    Parameters:
    array (np.ndarray): Input array.
    
    Returns:
    float: Standard deviation of all elements in the array.
    """
    return np.std(array)

#Variance of all elements in an array
def var_array_elements(array):
    """
    Calculate the variance of all elements in a numpy array.

    Parameters:
    array (np.ndarray): Input array.

    Returns:
    float: Variance of all elements in the array.
    """
    return np.var(array)

#Minimum value in an array
def min_array_elements(array):
    """
    Calculate the minimum value in a numpy array.

    Parameters:
    array (np.ndarray): Input array.

    Returns:
    float: Minimum value in the array.
    """
    return np.min(array)
#Maximum value in an array
def max_array_elements(array):  
    """
    Calculate the maximum value in a numpy array.

    Parameters:
    array (np.ndarray): Input array.

    Returns:
    float: Maximum value in the array.
    """
    return np.max(array)

#Range of values in an array
def range_array_elements(array):
    """
    Calculate the range of values in a numpy array.

    Parameters:
    array (np.ndarray): Input array.

    Returns:
    float: Range of values in the array (max - min).
    """
    return np.ptp(array)  # ptp stands for "peak to peak", which is max - min   

#Count of elements in an array
def count_array_elements(array):
    """
    Count the number of elements in a numpy array.

    Parameters:
    array (np.ndarray): Input array.

    Returns:
    int: Number of elements in the array.
    """
    return array.size

#Sum of elements along a specific axis
def sum_array_elements_axis(array, axis):
    """
    Calculate the sum of elements along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to sum the elements.

    Returns:
    np.ndarray: Sum of elements along the specified axis.
    """
    return np.sum(array, axis=axis)

#Mean of elements along a specific axis
def mean_array_elements_axis(array, axis):
    """
    Calculate the mean of elements along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to calculate the mean.

    Returns:
    np.ndarray: Mean of elements along the specified axis.
    """
    return np.mean(array, axis=axis)

# Median of elements along a specific axis
def median_array_elements_axis(array, axis):
    """
    Calculate the median of elements along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to calculate the median.

    Returns:
    np.ndarray: Median of elements along the specified axis.
    """
    return np.median(array, axis=axis)

# Standard deviation of elements along a specific axis
def std_array_elements_axis(array, axis):
    """
    Calculate the standard deviation of elements along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to calculate the standard deviation.

    Returns:
    np.ndarray: Standard deviation of elements along the specified axis.
    """
    return np.std(array, axis=axis)
# Variance of elements along a specific axis
def var_array_elements_axis(array, axis):
    """
    Calculate the variance of elements along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to calculate the variance.

    Returns:
    np.ndarray: Variance of elements along the specified axis.
    """
    return np.var(array, axis=axis)
# Minimum value along a specific axis
def min_array_elements_axis(array, axis):
    """
    Calculate the minimum value along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to find the minimum value.

    Returns:
    np.ndarray: Minimum value along the specified axis.
    """
    return np.min(array, axis=axis)

# Maximum value along a specific axis
def max_array_elements_axis(array, axis):
    """
    Calculate the maximum value along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to find the maximum value.

    Returns:
    np.ndarray: Maximum value along the specified axis.
    """
    return np.max(array, axis=axis)

# Range of values along a specific axis
def range_array_elements_axis(array, axis):
    """
    Calculate the range of values along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to calculate the range.

    Returns:
    np.ndarray: Range of values along the specified axis (max - min).
    """
    return np.ptp(array, axis=axis)  # ptp stands for "peak to peak", which is max - min

# Count of elements along a specific axis
def count_array_elements_axis(array, axis):
    """
    Count the number of elements along a specific axis in a numpy array.

    Parameters:
    array (np.ndarray): Input array.
    axis (int): Axis along which to count the elements.

    Returns:
    np.ndarray: Number of elements along the specified axis.
    """
    return np.count_nonzero(~np.isnan(array), axis=axis)  # Count non-NaN elements along the specified axis

# Example usage
if __name__ == "__main__":
    array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print("Sum of all elements:", sum_array_elements(array))
    print("Mean of all elements:", mean_array_elements(array))
    print("Median of all elements:", median_array_elements(array))
    print("Standard deviation of all elements:", std_array_elements(array))
    print("Variance of all elements:", var_array_elements(array))
    print("Minimum value in the array:", min_array_elements(array))
    print("Maximum value in the array:", max_array_elements(array))
    print("Range of values in the array:", range_array_elements(array))
    print("Count of elements in the array:", count_array_elements(array))
    
    axis = 0
    print(f"Sum along axis {axis}:", sum_array_elements_axis(array, axis))
    print(f"Mean along axis {axis}:", mean_array_elements_axis(array, axis))
    print(f"Median along axis {axis}:", median_array_elements_axis(array, axis))
    print(f"Standard deviation along axis {axis}:", std_array_elements_axis(array, axis))
    print(f"Variance along axis {axis}:", var_array_elements_axis(array, axis))
    print(f"Minimum value along axis {axis}:", min_array_elements_axis(array, axis))
    print(f"Maximum value along axis {axis}:", max_array_elements_axis(array, axis))
    print(f"Range of values along axis {axis}:", range_array_elements_axis(array, axis))
    print(f"Count of elements along axis {axis}:", count_array_elements_axis(array, axis))