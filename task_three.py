class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def sum_values(self):
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        if node is None:
            return 0
        return node.value + self._sum_recursive(node.left) + self._sum_recursive(node.right)

bst = BinarySearchTree()
bst.insert(50)
bst.insert(370)
bst.insert(7086)
bst.insert(20)
bst.insert(450)
bst.insert(60)
bst.insert(500)

total_sum = bst.sum_values()
print("Сума всіх значень у дереві:", total_sum)