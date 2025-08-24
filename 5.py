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
            if val == cur.val:   
                return
            elif val < cur.val:
                if cur.left: 
                    cur = cur.left
                else:
                    cur.left = Node(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = Node(val)
                    return
    def show_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        print(prefix + ("├─L─" if is_left else "├─R─") + str(node.val) if prefix else str(node.val))
        if node.left:
            self.show_tree(node.left, prefix + "│  ", True)
        if node.right:
            self.show_tree(node.right, prefix + "│  ", False)

if __name__ == "__main__":
    tree = SearchBinaryTree()
    data = [50, 77, 55, 29, 10, 50, 30, 66, 18, 80, 51, 18, 90]
    for t in data:
        tree.insert_normal(t)
    tree.show_tree()
