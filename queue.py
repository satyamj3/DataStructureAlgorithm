class Node:
    def __init__(self, data='', next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def push(self, value):
        if self.head == self.tail == None:
            self.head = self.tail = Node(value)
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def pop(self):
        if self.is_empty():
            print('Queue is empty')
            return
        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        return self.head.data

    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def is_empty(self):
        return self.head == self.tail == None

    def traverse(self):
        if self.is_empty():
            print('Queue is empty')
            return
        node = self.head
        while node:
            print('queue data:', node.data)
            node = node.next


queue = Queue()
data = [1, 4, 52, 6, 7, 34]
for dt in data:
    queue.push(dt)

queue.traverse()
print(queue.pop())
print(queue.pop())
queue.traverse()
