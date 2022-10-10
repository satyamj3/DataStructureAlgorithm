class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data, None)

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        node = self.head
        ll_data = ''
        while node:
            # print('data -> ', node.data)
            ll_data += str(node.data) + '-->'
            node = node.next
        print(ll_data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                print('removed', node.next.data)
                node.next = node.next.next
                break
            node = node.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        node = self.head
        while node:
            if count == index - 1:
                new_node = Node(data, node.next)
                node.next = new_node
                break
            count += 1
            node = node.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        node = self.head
        while node:
            if node.data == data_after:
                new_node = Node(data_to_insert, node.next)
                node.next = new_node
                return
            node = node.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.data == data:
                node.next = node.next.next
                return
            node = node.next
        raise Exception('Invalid data passed to remove')


if __name__ == '__main__':
    # ll = LinkedList()
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(10)
    # ll.print()
    # ll.insert_at_end(79)
    # ll.print()
    # ll.remove_at(1)
    # print('removed')
    # ll.print()
    # ll.insert_at(0, 345)
    # ll.print()
    # ll.insert_at(3, 3645)
    # ll.print()
    # print('length', ll.get_length())

    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    # ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
