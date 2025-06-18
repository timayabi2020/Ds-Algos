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