# Created by Jinwook Lim (Aiden Lim) at 11:48 PM 2021/04/20
__author__ = "Jinwook Lim (Aiden Lim)"


# Implement Stack using linked list

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    for _ in range(5):
        print(stack.pop())
