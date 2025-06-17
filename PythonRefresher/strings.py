# Here's an example of a string
my_string = "Hello, World!"
print(my_string)  # Output: Hello, World!

# Accessing characters in a string
print(my_string[0])  # Output: H
print(my_string[-1])  # Output: !

# Slicing a string
print(my_string[0:5])  # Output: Hello
print(my_string[7:])  # Output: World!

# String operations
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Output: Hello World
print(str1 * 3)  # Output: HelloHelloHello

# Repetition
print("Repeat" * 2)  # Output: RepeatRepeat

# Common string methods
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.replace("World", "Python"))  # Output: Hello, Python!
print(my_string.split(", "))  # Output: ['Hello', 'World!']

# Checking if a string contains a substring
print("Hello" in my_string)  # Output: True

# Checking string length
print(len(my_string))  # Output: 13

# Indexing and finding characters
print(my_string.index("W"))  # Output: 7

# Finding the position of a substring
print(my_string.find("World"))  # Output: 7

# Checking if a string starts or ends with a specific substring
print(my_string.startswith("Hello"))  # Output: True
print(my_string.endswith("!"))  # Output: True

# String formatting
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# f-string formatting (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# Multiline strings
multiline_string = """This is a string
that spans multiple lines.
"""
print(multiline_string)

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!

# String interpolation using f-strings
age = 30
full_greeting_f = f"{greeting}, {name}! You are {age} years old."
print(full_greeting_f)  # Output: Hello, Alice! You are 30 years old.