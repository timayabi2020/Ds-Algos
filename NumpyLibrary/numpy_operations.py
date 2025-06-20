# Add two npy arrays element-wise and return the result.
import numpy as np
def add_arrays(array1, array2):
    """
    Add two numpy arrays element-wise and return the result.
    
    Parameters:
    array1 (np.ndarray): First array to add.
    array2 (np.ndarray): Second array to add.
    
    Returns:
    np.ndarray: Element-wise sum of the two arrays.
    """
    if array1.shape != array2.shape:
        raise ValueError("Arrays must have the same shape for element-wise addition.")
    
    return np.add(array1, array2)

# Multiply two numpy arrays element-wise and return the result.
def multiply_arrays(array1, array2):
    """
    Multiply two numpy arrays element-wise and return the result.
    
    Parameters:
    array1 (np.ndarray): First array to multiply.
    array2 (np.ndarray): Second array to multiply.
    
    Returns:
    np.ndarray: Element-wise product of the two arrays.
    """
    if array1.shape != array2.shape:
        raise ValueError("Arrays must have the same shape for element-wise multiplication.")
    
    return np.multiply(array1, array2)

# Divide two numpy arrays element-wise and return the result.
def divide_arrays(array1, array2):
    """
    Divide two numpy arrays element-wise and return the result.
    
    Parameters:
    array1 (np.ndarray): Numerator array.
    array2 (np.ndarray): Denominator array.
    
    Returns:
    np.ndarray: Element-wise division of the two arrays.
    """
    if array1.shape != array2.shape:
        raise ValueError("Arrays must have the same shape for element-wise division.")
    
    if np.any(array2 == 0):
        raise ValueError("Division by zero encountered in one or more elements.")
    
    return np.divide(array1, array2)

# Example usage
if __name__ == "__main__":
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.array([[10, 20, 30], [40, 50, 60]])
    
    result = add_arrays(array1, array2)
    print("Element-wise addition result:\n", result)

    result = multiply_arrays(array1, array2)
    print("Element-wise multiplication result:\n", result)

    result = divide_arrays(array1, array2)
    print("Element-wise division result:\n", result)

    # Power operation on numpy arrays
    power_result = np.power(array1, 2)
    print("Element-wise power result:\n", power_result)

    # Modulus operation on numpy arrays
    modulus_result = np.mod(array2, 7)
    print("Element-wise modulus result:\n", modulus_result)

    #Exponentiation of a numpy array
    exp_result = np.exp(array1)
    print("Element-wise exponentiation result:\n", exp_result)

    # Logarithm of a numpy array
    log_result = np.log(array2)
    print("Element-wise logarithm result:\n", log_result)