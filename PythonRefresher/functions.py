# Function decorators. They are defined using the `@decorator_name` syntax and are used to modify the behavior of functions or methods. Here's a simple example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
# Example usage of the decorated function
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Higher-order functions are functions that can take other functions as arguments or return them as results. They are often used in functional programming paradigms. Here's an example of a higher-order function:
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x
# Example usage of the higher-order function
result = apply_function(square, 5)
print("Result of applying square function:", result)
# Output: Result of applying square function: 25

# Lambda functions are small anonymous functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression. Here's an example:
add = lambda x, y: x + y
# Example usage of the lambda function
result = add(3, 5)
print("Result of adding 3 and 5 using lambda:", result)
# Output: Result of adding 3 and 5 using lambda: 8

# Lambda functions can also be used in higher-order functions like `map`, `filter`, and `reduce`. Here's an example using `map`:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print("Squared Numbers:", squared_numbers)
# Output: Squared Numbers: [1, 4, 9, 16, 25]

# Using `filter` with a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)# Output: Even Numbers: [2, 4]
# Output: Even Numbers: [2, 4]
# Using `reduce` with a lambda function to calculate the product of numbers
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)
# Output: Product of Numbers: 120

