# Stack using python library deque and doubly link list (doubly has less complexity than singly linked list)

from collections import deque


class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Stack:
    def __init__(self):
        ## using deque
        self.container = deque()
        ## using doubly linked list
        self.head = None
        self.tail = None

    def push(self, value):
        try:
            ## using deque
            self.container.append(value)
            ## using doubly linked list
            node = Node(value)
            if self.head == self.tail == None:
                self.head = node
                self.tail = node
                return
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        except MemoryError:
            print("""Cannot push more element as the Memory is full
                    Last pushed element {}
            """.format(value))

    def pop(self):
        # deque
        elem = self.container.pop()
        # dlinked list
        if self.head == self.tail:
            self.head = self.tail = None
            return elem
        self.tail = self.tail.prev
        self.tail.next = None
        return elem

    def peek(self):
        print('Top element from Stack (Deque): {}'.format(self.container[-1]))
        print('Top element from Stack (LinkedList): {}'.format(self.tail.data))

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def is_empty(self):
        return self.size() == 0 and self.head == self.tail == None

    def traverse(self):
        print('Elements in Stack (Deque): {}'.format(', '.join(
            [str(elem) for elem in self.container])))
        node = self.head
        while node:
            print('Elements in Stack (LinkedList): {}'.format(node.data))
            node = node.next


stack = Stack()
elements = [1, 3, 5, 6, 8, 9, 12]
for elem in elements:
    stack.push(elem)

stack.traverse()
print(stack.pop())


def reverse_string(string):
    stack = Stack()
    for elem in string:
        stack.push(elem)
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()
    return rev_str


print(reverse_string("We will conquere COVI-19"))
print(reverse_string("I am the King"))


def is_balanced(string):
    print('string:', string)
    stack = Stack()
    paran_dict = {'}': '{', ']': '[', ')': '('}
    for elem in string:
        if elem in ['(', '{', '[']:
            stack.push(elem)
        elif elem in paran_dict:
            if stack.is_empty():
                return False
            else:
                if stack.pop() != paran_dict[elem]:
                    return False

    return True


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
