class MyClass():
    def set_age(self, num):
        self.age = num

    def get_age(self):
        return self.age
    
Sara = MyClass()
Sara.set_age(30)
print(Sara.get_age())  # Output: 30
