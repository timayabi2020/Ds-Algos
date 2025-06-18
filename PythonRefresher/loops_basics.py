# Loops in python

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
# Using range() to iterate over a sequence of numbers
for i in range(5):
    print(i)

# Output: 0
# 1
# 2
# 3
# 4

for i in range(len(fruits)):
    print(fruits[i])
# Output:
# apple 
# banana
# cherry

# Enumerate to get index and value
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
# Output:   Index: 0, Fruit: apple
#           Index: 1, Fruit: banana
#           Index: 2, Fruit: cherry

#Zipping two lists together
vegetables = ["carrot", "broccoli", "spinach"]
for fruit, vegetable in zip(fruits, vegetables):
    print(f"Fruit: {fruit}, Vegetable: {vegetable}")
# Output: Fruit: apple, Vegetable: carrot
#         Fruit: banana, Vegetable: broccoli
#         Fruit: cherry, Vegetable: spinach

# Iterating through a tuple
my_tuple = [(1, 2), (3, 4), (5, 6)]
for a, b in my_tuple:
    print(f"a: {a}, b: {b}")
# Output: a: 1, b: 2
#         a: 3, b: 4
#         a: 5, b: 6

dict = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in dict.items():
    print(f"{key}: {value}")

# Dictionary lets us conveniently access key-value pairs without indexing.

# Start, stop, step in range()
for i in range(1, 10, 2):  # Start at 1, stop before 10, step by 2
    print(i)

# Output: 1
# 3
# 5
# 7
# 9

# Use start stop loop backwards
for i in range(10, 0, -2):  # Start at 10, stop before 0, step by -2
    print(i)
# Output: 10
# 8
# 6
# 4
# 2
# Forward removal of elements in a list
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    my_list.remove(item)
print(my_list)  # Output: [] (all elements removed)

# Backward removal of elements in a list
my_list = [1, 2, 3, 4, 5]
for i in reversed(my_list):
    my_list.remove(i)
print(my_list)  # Output: [] (all elements removed)

# Find even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Breaking out of a loop
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
# Output: 0
# 1
# 2
# 3
# 4

# Continuing to the next iteration
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Output: 1
# 3 
# 5
# 7
# 9

#Itertools module for advanced looping
from itertools import product, permutations

for item in product([1, 2], ['a', 'b']):
    print(item)
# Output: (1, 'a')
#         (1, 'b')
#         (2, 'a')
#         (2, 'b')
for item in permutations([1, 2, 3]):
    print(item)
# Output: (1, 2, 3)
#         (1, 3, 2)
#         (2, 1, 3)
#         (2, 3, 1)
#         (3, 1, 2)
#         (3, 2, 1)
# Using itertools to create combinations
from itertools import combinations

for item in combinations([1, 2, 3, 4], 2):
    print(item)
# Output: (1, 2)
#         (1, 3)
#         (1, 4)
#         (2, 3)
#         (2, 4)
#         (3, 4)
# Using itertools to create combinations with replacement
from itertools import combinations_with_replacement

for item in combinations_with_replacement([1, 2, 3, 4], 2):
    print(item)
# Output: (1, 1)
#         (1, 2)
#         (1, 3)
#         (1, 4)
#         (2, 2)
#         (2, 3)
#         (2, 4)
#         (3, 3)
#         (3, 4)
#         (4, 4)
