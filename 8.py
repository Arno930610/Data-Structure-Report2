# 一、實現節點類
class Node:
    def __init__(self, val):
        self.val, self.left, self.right = val, None, None
# 二、實現二叉搜尋樹類
class BST:
    def __init__(self): 
        self.root = None
    # 三、二叉搜尋樹添加節點
    def insert(self, val):
        if not self.root: 
            self.root = Node(val); return
        cur = self.root
        while True:
            if val == cur.val: return         # 不插入重複值
            elif val < cur.val:
                if cur.left: cur = cur.left
                else: cur.left = Node(val); return
            else:
                if cur.right: cur = cur.right
                else: cur.right = Node(val); return
    # 四、二叉搜尋樹的額外功能：最大值和最小值
    def get_max(self):
        cur = self.root
        while cur.right: cur = cur.right
        return cur.val
    def get_min(self):
        cur = self.root
        while cur.left: cur = cur.left
        return cur.val
if __name__ == "__main__":
    tree = BST()
    data = [50, 77, 55, 29, 10, 30, 66, 18, 80, 51, 90]
    for v in data: tree.insert(v)

    print("二叉搜尋樹的最大值:", tree.get_max())  # 90
    print("二叉搜尋樹的最小值:", tree.get_min())  # 10
