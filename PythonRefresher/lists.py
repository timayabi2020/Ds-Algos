# List example
# Here's an example of a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Indexing and slicing a list
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5
print(my_list[1:4])  # Output: [2, 3, 4]

# Deleting elements from a list
del my_list[2]  # Deletes the element at index 2
print(my_list)  # Output: [1, 2, 4, 5]
last_element = my_list.pop()  # Removes and returns the last element
print(last_element)  # Output: 5
print(my_list)  # Output: [1, 2, 4]

#Update an element in a list
my_list[1] = 10  # Updates the element at index 1
print(my_list)  # Output: [1, 10, 4]

# Adding elements to a list
my_list.append(6)  # Appends 6 to the end of the list
print(my_list)  # Output: [1, 10, 4, 6]

# Inserting an element at a specific position
my_list.insert(1, 3)  # Inserts 3 at index 1
print(my_list)  # Output: [1, 3, 10, 4, 6]

# sorting a list
my_list.sort()  # Sorts the list in ascending order

print(my_list)  # Output: [1, 3, 4, 6, 10]

# Reversing a list
my_list.reverse()  # Reverses the order of the list
print(my_list)  # Output: [10, 6, 4, 3, 1]

# Iterating through a list
for item in my_list:
    print(item, end=' ')  # Output: 10 6 4 3 1
    print()  # New line after iteration

# List comprehension
squared_list = [x**2 for x in my_list]  # Creates a new list with squared values
print(squared_list)  # Output: [100, 36, 16, 9, 1]

# Convert to tuples 
my_tuple = tuple(my_list)  # Converts the list to a tuple
print(my_tuple)  # Output: (10, 6, 4, 3, 1)

# Convert to set
my_set = set(my_list)  # Converts the list to a set
print(my_set)  # Output: {1, 3, 4, 6, 10} (order may vary)

