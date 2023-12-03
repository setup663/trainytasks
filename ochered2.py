""""
Разработать класс "Очередь". Удалить положительные элементы из очереди.
 Разрешается использовать только функции: добавление в конец, удаление из начала, получение первого элемента без удаления, проверка на пустоту
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, item):
        temp = Node(item)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None

    def getFront(self):
        if self.isEmpty():
            return None
        return self.front.data

    def removePositiveElements(self):
        current = self.front
        prev = None
        while current is not None:
            if current.data > 0:
                if prev is None:
                    self.front = current.next
                else:
                    prev.next = current.next
                if current == self.rear:
                    self.rear = prev
            else:
                prev = current
            current = current.next

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()


q = Queue()
q.enqueue(10)
q.enqueue(-5)
q.enqueue(20)
q.enqueue(30)
q.enqueue(-8)
q.enqueue(5)

print("Очередь перед удалением положительных элементов:")
q.display()

q.removePositiveElements()
print("Очередь после удаления положительных элементов:")
q.display()
