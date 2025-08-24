class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, root, value):
        node = value if isinstance(value, Node) else Node(value)
        if self.root is None:
            self.root = node
            print(f"插入根節點: {node.data}")
            return node
        if root is None:
            print(f"插入節點: {node.data}")
            return node

        if node.data < root.data:
            print(f"值 {node.data} < {root.data}，插入到左子樹")
            root.left_child = self.insert(root.left_child, value)
            root.left_child.parent = root
        elif node.data > root.data:
            print(f"值 {node.data} > {root.data}，插入到右子樹")
            root.right_child = self.insert(root.right_child, value)
            root.right_child.parent = root
        else:
            print(f"值 {node.data} 已存在，不插入")

        return root
    def inorder(self, root):
        if root:
            self.inorder(root.left_child)
            print(root.data, end=" ")
            self.inorder(root.right_child)
if __name__ == "__main__":
    bst = BinarySearchTree()
    nums = [50, 30, 70, 20, 40, 60, 80]

    for num in nums:
        bst.insert(bst.root, num)

    print("\n中序遍歷輸出:")
    bst.inorder(bst.root)

