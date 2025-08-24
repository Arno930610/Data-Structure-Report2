class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None
class BST:
    def __init__(self): self.root = None

    def insert(self, val):
        if not self.root: self.root = Node(val); return
        cur = self.root
        while True:
            if val == cur.val: return   # 不插入重複值
            elif val < cur.val:
                if cur.left: cur = cur.left
                else: cur.left = Node(val); return
            else:
                if cur.right: cur = cur.right
                else: cur.right = Node(val); return
    def search(self, node, val):
        if not node: return False
        if node.val == val: return True
        return self.search(node.left, val) if val < node.val else self.search(node.right, val)
    def get_max(self, node):
        while node.right: node = node.right
        return node.val
    def get_min(self, node):
        while node.left: node = node.left
        return node.val
if __name__ == "__main__":
    tree = BST()
    data = [50, 77, 55, 29, 10, 50, 30, 66, 18, 80, 51, 18, 90]
    for t in data: tree.insert(t)
    print("查詢數值 50:", tree.search(tree.root, 50))
    print("查詢數值 500:", tree.search(tree.root, 500))
    print("二叉搜尋樹的最大值:", tree.get_max(tree.root))
    print("二叉搜尋樹的最小值:", tree.get_min(tree.root))
