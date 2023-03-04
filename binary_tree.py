class BinarySearchTree:
    def __init__(self, data=None, parent=None, left=None, right=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.data = data

    def add_element(self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.left:
                self.left.add_element(data)  # when left node is not leaf node
            else:
                self.left = BinarySearchTree(
                    data)  # when the left node is the leaf node
        else:
            if self.right:
                self.right.add_element(
                    data)  # when right node is not a leaf node
            else:
                self.right = BinarySearchTree(
                    data)  # when the right node is the leaf node

    def print_tree(self):
        print(self.data)
        if self.left:
            print('left')
            self.left.print_tree()
        if self.right:
            print('right')
            self.right.print_tree()

    def in_order_traverse(self):
        """
        Order of traversal:
            Left node -> Head/Root node -> Right node
        """
        elements = []
        # left traverse:
        if self.left:
            elements += self.left.in_order_traverse()
        # checking the root
        # if self.data:
        elements.append(self.data)
        # right traverse:
        if self.right:
            elements += self.right.in_order_traverse()

        return elements

    def pre_order_traverse(self):
        """
        Order of traversal:
            Head/Root node -> Left node -> Right node
        """
        elements = []
        # checking the root
        # if self.data:
        elements.append(self.data)
        # left traverse:
        if self.left:
            elements += self.left.pre_order_traverse()
        # right traverse:
        if self.right:
            elements += self.right.pre_order_traverse()

        return elements

    def post_order_traverse(self):
        """
        Order of traversal:
            Left node -> Right node  -> Head/Root node
        """
        elements = []
        # left traverse:
        if self.left:
            elements += self.left.post_order_traverse()
        # right traverse:
        if self.right:
            elements += self.right.post_order_traverse()
        # checking the root
        # if self.data:
        elements.append(self.data)

        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.find_max()

    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_node(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        return self


def build_bst(data):
    root = BinarySearchTree(data[0])
    for dt in data:
        root.add_element(dt)
    return root


data = [23, 45, 12, 56, 3, 41, 1, 3, 90]
print(data)
root = build_bst(data)
root.print_tree()
print('this is the root: ', root.data)
print("Inoreder Traversal", root.in_order_traverse())
print("Preoreder Traversal", root.pre_order_traverse())
print("Postoreder Traversal", root.post_order_traverse())
print(root.delete_node(56))
# root.delete_node(45)
print("Inoreder Traversal", root.in_order_traverse())
print("Preoreder Traversal", root.pre_order_traverse())
print("Postoreder Traversal", root.post_order_traverse())
