class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, data):
        node = Node(data, self.head)
        if self.head is None:
            self.head = self.tail = node
            self.length += 1
            return
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, data):
        if self.head is None:
            self.head = self.tail = Node(data, None)
            self.length += 1
            return
        self.tail.next = Node(data, None)
        self.tail = self.tail.next
        self.length += 1

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        node = self.head
        ll_data = ''
        while node:
            ll_data += str(node.data) + '-->'
            node = node.next
        print(ll_data)

    def remove(self, index):
        if index < 0 or index >= self.length:
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        # count = 0
        node = self.head
        for _ in range(index - 1):
            node = node.next

        node.next = node.next.next
        self.length -= 1

    def pop(self):
        if self.head is None:
            raise Exception('EmptyLinkedList Error')
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
            return
        node = self.head
        print('Length:', self.length)
        for _ in range(self.length - 2):
            print('traversing: ', node)
            node = node.next
        # this is the just last element
        print('element after for loop: ', node)
        print('popping :', node.next)
        node.next = None

    def insert(self, index, data):
        if index < 0 or index > self.length:
            raise Exception('Invalid Index')

        if index == 0:
            self.prepend(data)
            return

        node = self.head
        for _ in range(index - 1):
            node = node.next
        new_node = Node(data, node.next)
        new_node.next = node.next
        node.next = new_node
        self.length += 1

    def insert_values(self, data_list):
        for data in data_list:
            self.append(data)

    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        self.head = prev

    # def sort(self, by_value=True):
    #     current_elem = self.head
    #     if by_value:
    #         while current_elem:
    #             check_elem = current_elem.next
    #             while check_elem:
    #                 if check_elem.data < current_elem.data:
    #                     check_elem.data, current_elem.data = current_elem.data, check_elem.data
    #                 check_elem = check_elem.next
    #             current_elem = current_elem.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.pop()
    ll.prepend(10)
    ll.append(79)
    ll.insert(0, 345)
    ll.insert(3, 3645)
    ll.print()
    ll.pop()
    ll.print()
