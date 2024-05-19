import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class AVLTreeNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)
        return root

class AVLTree(BinarySearchTree):
    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        self._update_height(z)
        self._update_height(y)

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)

        return y

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if not root:
            return AVLTreeNode(key)
        if key < root.key:
            root.left = self._insert_rec(root.left, key)
        elif key > root.key:
            root.right = self._insert_rec(root.right, key)

        self._update_height(root)

        balance = self._balance_factor(root)

        if balance > 1 and key < root.left.key:
            return self._rotate_right(root)

        if balance < -1 and key > root.right.key:
            return self._rotate_left(root)

        if balance > 1 and key > root.left.key:
            root.left = self._rotate_left(root.left)
            return self._rotate_right(root)

        if balance < -1 and key < root.right.key:
            root.right = self._rotate_right(root.right)
            return self._rotate_left(root)

        return root

def find_max_value_in_tree(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.key

def plot_tree(ax, node, x, y, dx, dy):
    if node is None:
        return
    ax.text(x, y, str(node.key), style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    if node.left:
        ax.add_patch(FancyArrowPatch((x, y), (x - dx, y - dy), connectionstyle="arc3,rad=.5", arrowstyle='->'))
        plot_tree(ax, node.left, x - dx, y - dy, dx / 2, dy)
    if node.right:
        ax.add_patch(FancyArrowPatch((x, y), (x + dx, y - dy), connectionstyle="arc3,rad=-.5", arrowstyle='->'))
        plot_tree(ax, node.right, x + dx, y - dy, dx / 2, dy)

# Тест:
avl_tree = AVLTree()
avl_tree.insert(50)
avl_tree.insert(30)
avl_tree.insert(70)
avl_tree.insert(20)
avl_tree.insert(40)
avl_tree.insert(60)
avl_tree.insert(80)
avl_tree.insert(90)
avl_tree.insert(10)
avl_tree.insert(55)
avl_tree.insert(75)

print("Найбільше значення в AVL-дереві:", find_max_value_in_tree(avl_tree.root))

fig, ax = plt.subplots(figsize=(8, 8))
plot_tree(ax, avl_tree.root, 0, 0, 30, 30)
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 0)
ax.axis('off')
plt.show()
