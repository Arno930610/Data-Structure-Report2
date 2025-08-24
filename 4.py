class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def is_empty(self):
        return self.root is None
    def insert_normal(self, value):
        """二叉搜尋樹插入節點 - 非遞迴 (帶輸出結果)"""
        node = value if isinstance(value, Node) else Node(value)

        if self.is_empty():
            self.root = node
            print(f"插入根節點: {node.data}")
        else:
            current_node = self.root
            while True:
                if node.data < current_node.data:
                    if current_node.left_child:
                        current_node = current_node.left_child
                    else:
                        current_node.left_child = node
                        node.parent = current_node
                        print(f"插入節點: {node.data} 到 {current_node.data} 的左子樹")
                        break
                elif node.data > current_node.data:
                    if current_node.right_child:
                        current_node = current_node.right_child
                    else:
                        current_node.right_child = node
                        node.parent = current_node
                        print(f"插入節點: {node.data} 到 {current_node.data} 的右子樹")
                        break
                else:
                    print(f"值 {node.data} 已存在，不插入")
                    break
        print("目前樹的中序遍歷:", end=" ")
        self.inorder(self.root)
        print("\n")  # 換行
        return node
    def inorder(self, root):
        if root:
            self.inorder(root.left_child)
            print(root.data, end=" ")
            self.inorder(root.right_child)
if __name__ == "__main__":
    bst = BinarySearchTree()
    nums = [50, 30, 70, 20, 40, 60, 80]
    for num in nums:
        bst.insert_normal(num)
