class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

# Рекурсивний метод, за допомогою якого ми шукаємо вершину, до якої
# додаємо нову об'єкт obj.
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

# Метод додавання вершин в бінарне дерево
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

# Метод видалення вершини s, якщо вона листова (без нащадків)
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

# Метод видалення вершини s, якщо у неї один нащадок
    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

# Метод видалення вершини бінарного дерева
    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)

        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)

        # умова, що виконується, якщо видаляється вершина з двома нащадками
        else:
            sr, pr, = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def min_value_node(self, data):
        current = data
        while current.left is not None:
            current = current.left

        return current.data

    def max_value_node(self, data):
        current = data
        while current.right is not None:
            current = current.right

        return current.data



v = [18, 34, 5, 7, 12, 16, 13, 22, 8, 20, 99, 5]

t = Tree()
for x in v:
    t.append(Node(x))
t.del_node(34)
t.show_tree(t.root)

print(f"min value node = {t.min_value_node(t.root)}")
print(f"max value node = {t.max_value_node(t.root)}")










