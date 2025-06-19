class UserData():
    age = 0
    name = None
    def __init__(self, age, name):
        self.age = age
        self.name = name
user_2 = UserData(30, "Bob")

class PhoneNum(UserData):
   def __init__(self, age, name, phone):
       super().__init__(age, name)
       self.phone = phone 

user_1 = PhoneNum(25, "Alice", "123-456-7890")

user_2 = PhoneNum(60, "Bob", "987-654-3210")

user_2.age  # Output: 60