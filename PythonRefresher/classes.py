class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"The value is: {self.value}")

# Example usage
if __name__ == "__main__":
    obj = MyClass(42)
    obj.display()