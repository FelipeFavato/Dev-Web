class ListaArray:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data.insert(index, value)

    def update(self, index, new_value):
        self.data[index] = new_value


array = ListaArray()
array.set(0, 'Felipe')
array.set(1, 'Ana')
array.set(2, 'Shirley')
array.set(3, 'Miguel')
array.update(1, 'Joao')


print(array)

index = 0
while index < len(array):
    print('index:', index, ', Nome:', array.get(index))
    index += 1
