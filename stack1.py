""""
Разработать класс "Стек". Отпечатать все нечетные числа стека. Разрешается использовать только push, pop, empty.
 После печати стек должен сохранить свое состояние. Примечание. Воспользоваться вторым стеком.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.data

    def empty(self):
        return self.top is None

    def print_odd_numbers(self):
        temp_stack = Stack()  # Создаем второй временный стек
        current = self.top
        while current is not None:
            if current.data % 2 != 0:  # Если число нечетное, печатаем и кладем во второй стек
                print(current.data, end=(" "))
                temp_stack.push(current.data)
            current = current.next

        # Восстановление исходного стека
        while not temp_stack.empty():
            self.push(temp_stack.pop())


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

print("Нечетные числа стека:")
s.print_odd_numbers()

print("Состояние стека после отображения нечетных чисел:")
current = s.top
while current is not None:
    print(current.data, end=(" "))
    current = current.next