from abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def search(self, index):
        return self.queue[index]

    def is_empty(self):
        return not len(self.queue)


lista = Queue()
print(lista.queue)
print(lista.is_empty())
lista.enqueue(2)
lista.enqueue(5)
lista.enqueue(8)
lista.enqueue(4)
lista.enqueue(9)
print(lista.queue)
print(lista.search(0))
print(lista.is_empty())
