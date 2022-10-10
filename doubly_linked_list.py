class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_head(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data, None, self.head)
            self.head.prev = new_node
            self.head = new_node

    def add_tail(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def add(self, new_node, node_idx=None):
        if not self.head or node_idx == 1:
            self.add_head(new_node)
        else:
            self.last.next = new_node
            self.last = new_node
        self.count += 1
