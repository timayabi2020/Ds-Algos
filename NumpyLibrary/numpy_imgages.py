import numpy as np

# Convert an image to a numpy array
def image_to_numpy(image):
    """
    Convert an image to a numpy array.
    
    Parameters:
    image (PIL.Image): Input image.
    
    Returns:
    np.ndarray: Numpy array representation of the image.
    """
    return np.array(image)

# Convert a numpy array to an image
def numpy_to_image(array):
    """
    Convert a numpy array to an image.
    
    Parameters:
    array (np.ndarray): Input numpy array.
    
    Returns:
    PIL.Image: Image representation of the numpy array.
    """
    from PIL import Image
    return Image.fromarray(array.astype('uint8'))

#Example usage
if __name__ == "__main__":
    from PIL import Image
    # Load an image using PIL
    image = Image.open('passport.jpg')
    
    # Convert the image to a numpy array
    array = image_to_numpy(image)
    print("Numpy Array Shape:", array.shape)
    
    # Convert the numpy array back to an image
    new_image = numpy_to_image(array)
    new_image.show()  # Display the image