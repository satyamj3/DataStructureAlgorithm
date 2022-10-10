class SLinkedList:
    def __init__(self, head=None):
        self.count = 0
        self.head = head
        self.tail = None

    def traverse(self):
        next = self.head
        if not next:
            print('No element to traverse from an empty Linked list')
            return
        while next is not None:
            print(next.value)
            next = next.next
        return

    def add_head(self, node):
        if not self.head:
            print(f'Head added {node.value}')
            self.tail = node
        else:
            print(f'Head replaced by {node.value}')
            node.next = self.head
        self.head = node
        return
            
    def add(self, data, node_idx=None):
        new_node = Node(data)
        if not self.head or node_idx == 1:    # if the node to be added as head
            self.add_head(new_node)
        else:
            # add element to last if node index is not given
            self.tail.next = new_node
            self.tail = new_node
            print(f'Added element {data}')
        self.count += 1
        return

    def search(self, node_idx):
        if node_idx > self.count:
            print(f"node index {node_idx} is Invalid")
            return None
        current_node = self.head
        if node_idx and node_idx < self.count:
            current_node_idx = 1
            while current_node_idx < node_idx:
                current_node = current_node.next
                current_node_idx += 1
            print(f'The {node_idx} element')
            return current_node
        else:    # return the last node
            return self.tail

    def remove(self, node_idx):
        if not self.head:
            print('Cannot delete element from an empty Linked list')
        elif node_idx == 1:    # if the element is head
            self.head = None
            self.count -= 1
        else:
            prev_node = self.search(node_idx-1)
            current_node = prev_node.next
            print(f'Removing element {current_node.value}')
            if not current_node.next: # if the element is the last
                prev_node.next = None
            else:
                prev_node.next = current_node.next
            del current_node
            self.count -= 1
        return

    def update(self, node_idx, new_value=None):
        node = self.search(node_idx)
        node.value = new_value
        return

    def view(self, node_idx):
        node = self.search(node_idx)
        print(f"Node value at index {node_idx} is {node.value}")
        return

    def sort(self):
        pass

    def length(self):
        return self.count


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

print('begin')
llist1 = SLinkedList()
llist1.add(2)
llist1.add("Tue")
llist1.add("Wed", 1)
llist1.traverse()
print('stop')
print(llist1.length())
llist1.remove(2)
llist1.traverse()
