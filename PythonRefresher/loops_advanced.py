# Iterative approach

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Recursive approach
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
# Example usage
n = 5
print("Iterative Factorial of", n, "is:", factorial_iterative(n))
print("Recursive Factorial of", n, "is:", factorial_recursive(n))

# Using a while loop to calculate factorial
def factorial_while(n):
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

# Example usage of while loop factorial
print("While Loop Factorial of", n, "is:", factorial_while(n))

# Square numbers using a for loop
def square_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers
# Example usage of square_numbers function
numbers = [1, 2, 3, 4, 5]
print("Squared Numbers:", square_numbers(numbers))

# while loop with boolean condition
def count_down(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

# Example usage of count_down function
count_down(5)
# Using a for loop with range
def count_up_to(n):
    for i in range(1, n + 1):
        print(i)
# Example usage of count_up_to function

count_up_to(5)

# An idiomatic pattern is while True with a break condition
def infinite_loop_with_break():
    i = 0
    while True:
        print(i)
        i += 1
        if i >= 5:  # Break condition
            break
        print("Still running...")

# Example usage of infinite_loop_with_break function
infinite_loop_with_break()

# Using a while loop in collections
def collect_even_numbers(limit):
    even_numbers = []
    i = 0
    while i <= limit:
        if i % 2 == 0:
            even_numbers.append(i)
        i += 1
    return even_numbers
# Example usage of collect_even_numbers function
limit = 10
print("Even Numbers up to", limit, ":", collect_even_numbers(limit))


