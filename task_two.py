class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Вставка нового вузла в дерево
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        # Рекурсивна допоміжна функція для вставки
        if value < current.value:
            # Йдемо в ліве піддерево
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            # Йдемо в праве піддерево
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    def find_min_value(self):
        # Функція для знаходження найменшого значення
        if self.root is None:
            return None  # Повертаємо None, якщо дерево порожнє
        
        current = self.root
        # Переходимо до самого лівого вузла
        while current.left is not None:
            current = current.left
        
        return current.value


bst = BinarySearchTree()
bst.insert(50)
bst.insert(370)
bst.insert(7086)
bst.insert(20)
bst.insert(450)
bst.insert(60)
bst.insert(500)

min_value = bst.find_min_value()
print("Найменше значення в дереві:", min_value)