# This script demonstrates the use of the type() function in Python to check the data types of various values.
type(105)
print(type(105))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("Hello, World!"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({1, 2, 3}))  # <class 'set'>
print(type({"key": "value"}))  # <class 'dict'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>
print(type(105.0))  # <class 'float'>
print(type(3 + 4j))  # <class 'complex'>
print(type(b"byte string"))  # <class 'bytes'>
print(type(bytearray(b"byte array")))  # <class 'bytearray'>
print(type(memoryview(b"memory view")))  # <class 'memoryview'>
print(type(range(10)))  # <class 'range'>
print(type(frozenset([1, 2, 3])))  # <class 'frozenset'>
print(type({1, 2, 3, 4}))  # <class 'set'>
print(type({1: "one", 2: "two"}))  # <class 'dict'>