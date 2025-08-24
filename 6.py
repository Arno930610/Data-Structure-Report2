from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class SearchBinaryTree:
    def __init__(self):
        self.root = None
    def insert_normal(self, val):
        if not self.root:
            self.root = Node(val)
            return
        cur = self.root
        while True:
            if val == cur.val: return  # 不插入重複值
            elif val < cur.val:
                if cur.left: cur = cur.left
                else: cur.left = Node(val); return
            else:
                if cur.right: cur = cur.right
                else: cur.right = Node(val); return
    def levelorder_traversal(self):
        if not self.root: return
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.val, end=' ')
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    def preorder_traversal(self, node):
        if not node: return
        print(node.val, end=' ')
        self.preorder_traversal(node.left)
        self.preorder_traversal(node.right)
    def inorder_traversal(self, node):
        if not node: return
        self.inorder_traversal(node.left)
        print(node.val, end=' ')
        self.inorder_traversal(node.right)
    def postorder_traversal(self, node):
        if not node: return
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.val, end=' ')
if __name__ == "__main__":
    tree = SearchBinaryTree()
    data = [50, 77, 55, 29, 10, 50, 30, 66, 18, 80, 51, 18, 90]
    for t in data:
        tree.insert_normal(t)
    print('層次遍歷: ', end='')
    tree.levelorder_traversal(); print()
    print('先序遍歷: ', end='')
    tree.preorder_traversal(tree.root); print()
    print('中序遍歷: ', end='')
    tree.inorder_traversal(tree.root); print()
    print('後序遍歷: ', end='')
    tree.postorder_traversal(tree.root); print()
