class Employee:
    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name


class HashMap:
    def __init__(self):
        # Cria uma lista de listas vazias, para cada i
        # em um range de 0 a 9, tem-se uma lista vazia
        self._buckets = [[] for i in range(10)]

    def __str__(self):
        return f'{self._buckets}'

    def get_address(self, id_num):
        return id_num % 10

    def insert(self, employee):
        # Variavel auxiliar armazena o valor da função
        address = self.get_address(employee.id_num)
        # Essa variável é usada como chave para armazenar o
        # objeto employee
        self._buckets[address].append(employee)

    def get_value(self, id_num):
        # Recebe o id, joga na função get_address
        # retorna o address
        address = self.get_address(id_num)
        for item in self._buckets[address]:
            if item.id_num == id_num:
                return item.name
        return None

    def has(self, id_num):
        address = self.get_address(id_num)
        return self._buckets[address] is not None

    # Não esta atualizada para [[],[], ...]
    def update_value(self, id_num, new_name):
        address = self.get_address(id_num)
        self._buckets[address].name = new_name


employees = [(14, 'name1'), (23, 'name2'), (10, 'name3'), (9, 'name4')]
registry = HashMap()

for id_num, name in employees:
    employee = Employee(id_num, name)
    registry.insert(employee)

print(registry.get_value(23))
