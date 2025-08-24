class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
class SearchBinaryTree(object):
    """二叉樹類"""
    def __init__(self):
        self.__root = None
        self.prefix_branch = '├'
        self.prefix_trunk = '│'
        self.prefix_leaf = '└'
        self.prefix_empty = ' '
        self.prefix_left = '─L─'
        self.prefix_right = '─R─'
    def is_empty(self):
        return not self.__root
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self, value):
        self.__root = value if isinstance(value, Node) else Node(value)
    def show_tree(self):
        if self.is_empty():
            print("空二叉樹")
            return
        print(self.__root.data)
        self.__print_tree(self.__root)
        print(' ' * 28)
    def levelorder_traversal(self):
        """層序遍歷"""
        if self.is_empty():
            return
        queue = list()
        queue.insert(0, self.__root)
        while len(queue):
            cur = queue.pop()
            print(cur.data, end=' ')
            if cur.left_child is not None:
                queue.insert(0, cur.left_child)
            if cur.right_child is not None:
                queue.insert(0, cur.right_child)
        print()
    def preorder_traversal(self, node):
        """先序遍歷"""
        if node is None:
            return
        print(node.data, end=' ')
        self.preorder_traversal(node.left_child)
        self.preorder_traversal(node.right_child)
    def inorder_traversal(self, node):
        """中序遍歷"""
        if node is None:
            return
        self.inorder_traversal(node.left_child)
        print(node.data, end=' ')
        self.inorder_traversal(node.right_child)
    def postorder_traversal(self, node):
        """後序遍歷"""
        if node is None:
            return
        self.postorder_traversal(node.left_child)
        self.postorder_traversal(node.right_child)
        print(node.data, end=' ')
    def __print_tree(self, node, prefix=None):
        if prefix is None:
            prefix, prefix_left_child = '', ''
        else:
            prefix = prefix.replace(self.prefix_branch, self.prefix_trunk)
            prefix = prefix.replace(self.prefix_leaf, self.prefix_empty)
            prefix_left_child = prefix.replace(self.prefix_leaf, self.prefix_empty)
        if self.has_child(node):
            if node.right_child is not None:
                print(prefix + self.prefix_branch + self.prefix_right + str(node.right_child.data))
                if self.has_child(node.right_child):
                    self.__print_tree(node.right_child, prefix + self.prefix_branch + ' ')
            else:
                print(prefix + self.prefix_branch + self.prefix_right)
            if node.left_child is not None:
                print(prefix + self.prefix_leaf + self.prefix_left + str(node.left_child.data))
                if self.has_child(node.left_child):
                    prefix_left_child += ' '
                    self.__print_tree(node.left_child, self.prefix_leaf + prefix_left_child)
            else:
                print(prefix + self.prefix_leaf + self.prefix_left)
    def has_child(self, node):
        return node.left_child is not None or node.right_child is not None
    def __str__(self):
        return str(self.__class__)
if __name__ == '__main__':
    tree = SearchBinaryTree()

    # 建立一棵簡單的二叉樹
    tree.root = Node(1)
    tree.root.left_child = Node(2)
    tree.root.right_child = Node(3)
    tree.root.left_child.left_child = Node(4)
    tree.root.left_child.right_child = Node(5)
    tree.root.right_child.left_child = Node(6)
    tree.root.right_child.right_child = Node(7)

    # 顯示樹狀結構
    print("樹狀結構:")
    tree.show_tree()

    # 層序遍歷
    print("層序遍歷:")
    tree.levelorder_traversal()

    # 先序遍歷
    print("先序遍歷:")
    tree.preorder_traversal(tree.root)
    print()

    # 中序遍歷
    print("中序遍歷:")
    tree.inorder_traversal(tree.root)
    print()

    # 後序遍歷
    print("後序遍歷:")
    tree.postorder_traversal(tree.root)
    print()
