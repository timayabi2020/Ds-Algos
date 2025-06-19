# Function caching is a technique to store the results of expensive function calls and return the cached result when the same inputs occur again. This can significantly improve performance, especially for recursive functions. Here's an example of a simple memoization decorator:

import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 10:", fibonacci(10))  # Output: Fibonacci of 10: 55
print("Fibonacci of 20:", fibonacci(20))  # Output: Fibonacci of 20: 6765

# Memoization is particularly useful for recursive functions where the same calculations are performed multiple times. The `lru_cache` decorator from the `functools` module automatically caches the results of the function calls, making subsequent calls with the same arguments much faster.
# This example demonstrates how memoization can optimize the performance of recursive functions by avoiding redundant calculations.

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper

@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))  # Output: Factorial of 5: 120
print("Factorial of 6:", factorial(6))  # Output: Factorial of 6: 720