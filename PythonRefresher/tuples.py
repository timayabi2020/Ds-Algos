# Here's an example of a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: 5
print(my_tuple[1:4])  # Output: (2, 3, 4)

# Tuples are immutable, so we cannot change their elements
# my_tuple[1] = 10  # This will raise a TypeError

# Adding elements to a tuple (creates a new tuple)
new_tuple = my_tuple + (6,)  # Adds 6 to the end of the tuple
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Tuples can be concatenated
another_tuple = (7, 8, 9)
combined_tuple = my_tuple + another_tuple
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8, 9)

# Tuples can be repeated
repeated_tuple = my_tuple * 2  # Repeats the tuple twice
print(repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking if an element exists in a tuple
print(3 in my_tuple)  # Output: True
print(10 in my_tuple)  # Output: False

# Length of a tuple
print(len(my_tuple))  # Output: 5

# Iterating through a tuple
for item in my_tuple:
    print(item, end=' ')  # Output: 1 2 3 4 5
    print()  # New line after iteration

# Tuple unpacking
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Output: 1 2 3 4 5

