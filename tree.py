class TreeNode:
    def __init__(self, name):
        self.name = name
        self.child = []
        self.parent = None

    def append(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        node = self
        while node:
            node = node.parent
            level += 1
        return level

    def print_tree(self, level=0):
        # print('{0}{1}'.format(' ' * level + '|__ ' if level != 0 else '',
        #                       self.name))

        print('{0}{1}'.format(
            ' ' * self.get_level() * 4 + '|__ ' if level != 0 else '',
            self.name))
        for child in self.child:
            child.print_tree(level + 1)

    def print_by_level(self, level=0):
        node_level = self.get_level()
        if node_level > level:
            return
        print('{0}{1}'.format(' ' * node_level * 2 + '|__ ', self.name))
        for child in self.child:
            child.print_by_level(level + 1)


def build_tree():
    root = TreeNode('Electronics')
    phones = TreeNode('Phones')
    phones.append(TreeNode('Apple'))
    phones.append(TreeNode('Samsung'))
    phones.append(TreeNode('Google'))

    appliances = TreeNode('Appliances')
    appliances.append(TreeNode('Samsung'))
    appliances.append(TreeNode('LG'))

    root.append(phones)
    root.append(appliances)
    return root


if __name__ == "__main__":
    root = build_tree()
    root.print_by_level(1)
