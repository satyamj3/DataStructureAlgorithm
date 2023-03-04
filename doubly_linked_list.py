class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)


class DLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def add_head(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        if self.head is None:
            self.add_head(value)
            return
        new_node = Node(value)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, value):
        if self.head is None:
            self.add_head(value)
            return
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def insert(self, index, value):
        pass

    def remove(self, index):
        pass

    def pop(self):
        pass

    def reverse(self):
        pass

    """
    def add_head(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value, None, self.head)
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def add(self, new_node, node_idx=None):
        if not self.head or node_idx == 1:
            self.add_head(new_node)
        else:
            self.last.next = new_node
            self.last = new_node
        self.count += 1
    """
