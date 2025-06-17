#Creating a dictionary in Python

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

#Adding a new key-value pair to the dictionary
my_dict["occupation"] = "Engineer"
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}

#Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30
#Accessing a key that does not exist using get() returns None
print(my_dict.get("country"))  # Output: None
#Accessing a key that does not exist using [] raises a KeyError
# print(my_dict["country"])  # Uncommenting this line will raise a KeyError

#Checking if a key exists in the dictionary
print("name" in my_dict)  # Output: True
print("country" in my_dict)  # Output: False

#Removing a key-value pair from the dictionary
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}

#Iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")

