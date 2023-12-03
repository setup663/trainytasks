""""
Разработать класс "Очередь". Даны две непустые очереди. Очереди содержат одинаковое количество элементов.
 Объединить очереди в одну, в которой элементы исходных очередей чередуются (начиная с первого элемента первой очереди).
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.data

    def merge_alternating(self, queue2):
        new_queue = Queue()
        current1 = self.head
        current2 = queue2.head
        while current1 is not None:
            new_queue.enqueue(current1.data)
            if current2 is not None:
                new_queue.enqueue(current2.data)
                current2 = current2.next
            current1 = current1.next
        return new_queue


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)

q2 = Queue()
q2.enqueue('a')
q2.enqueue('b')
q2.enqueue('c')

merged_queue = q1.merge_alternating(q2)

# Вывод результатов
print("Содержимое объединенной очереди:")
current = merged_queue.head
while current is not None:
    print(current.data, end=(" "))
    current = current.next
