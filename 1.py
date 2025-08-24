# coding=utf-8
class Node(object):
    """節點類"""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.parent = None
        self.left_child = left_child
        self.right_child = right_child

# 測試：建立節點
if __name__ == "__main__":
    root = Node(10)                     # 建立根節點
    root.left_child = Node(5)           # 建立左子節點
    root.right_child = Node(20)         # 建立右子節點
    root.left_child.parent = root       # 左子節點的父節點
    root.right_child.parent = root      # 右子節點的父節點

    # 輸出結果
    print("根節點:", root.data)
    print("左子節點:", root.left_child.data)
    print("右子節點:", root.right_child.data)
    print("左子節點的父節點:", root.left_child.parent.data)
    print("右子節點的父節點:", root.right_child.parent.data)
