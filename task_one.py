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

    def find_max_value(self):
        if self.root is None:
            return None  
        
        current = self.root
        while current.right is not None:
            current = current.right
        
        return current.value

bst = BinarySearchTree()
bst.insert(50)
bst.insert(370)
bst.insert(7086)
bst.insert(20)
bst.insert(450)
bst.insert(60)
bst.insert(500)

max_value = bst.find_max_value()
print("Найбільше значення в дереві:", max_value)
