class DataUser():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"DataUser with data: {self.data}"

    def __repr__(self):
        return f"DataUser({self.data!r})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __contains__(self, item):
        return item in self.data
    
    def __iter__(self):
        return iter(self.data)
    
    def __next__(self):
        return next(iter(self.data))
    def __add__(self, other):
        if isinstance(other, DataUser):
            return DataUser(self.data + other.data)
        return NotImplemented
    
    def __sub__(self, other):
        if isinstance(other, DataUser):
            return DataUser([item for item in self.data if item not in other.data])
        return NotImplemented
    

    def __mul__(self, other):
        if isinstance(other, int):
            return DataUser(self.data * other)
        return NotImplemented

# Example of using dunder methods
if __name__ == "__main__":
    data1 = DataUser([1, 2, 3])
    data2 = DataUser([3, 4, 5])
    print(data1 + data2)  # Output: DataUser with data: [1, 2, 3, 3, 4, 5]
    print(data1 - data2)  # Output: DataUser with data: [1, 2]
    print(data1 * 2)      # Output: DataUser with data: [1, 2, 3, 1, 2, 3]
    print(len(data1))     # Output: 3

