# Here is an example of a set in Python:
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements after creation.

my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding elements to a set
my_set.add(6)  # Adds 6 to the set
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)  # Removes 3 from the set
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Discarding elements from a set (does not raise an error if the element is not found)
my_set.discard(10)  # Does nothing since 10 is not in the set
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Checking if an element is in a set
print(2 in my_set)  # Output: True
print(10 in my_set)  # Output: False

# Union of sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_union = set_a.union(set_b)  # or set_a | set_b
print(set_union)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
set_intersection = set_a.intersection(set_b)  # or set_a & set_b
print(set_intersection)  # Output: {3}

# Difference of sets
set_difference = set_a.difference(set_b)  # or set_a - set_b
print(set_difference)  # Output: {1, 2}

# Symmetric difference of sets
set_symmetric_difference = set_a.symmetric_difference(set_b)  # or set_a ^ set_b
print(set_symmetric_difference)  # Output: {1, 2, 4, 5}

# Iterating through a set
for item in my_set:
    print(item, end=' ')  # Output: 1 2 4 5 6
print()  # New line after iteration