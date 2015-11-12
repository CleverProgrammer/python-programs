"""
creating a binary tree class and its methods
"""


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right


def preorderRecursive(root, result=[]):
    if not root:
        return

    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)
    return result


def inorderRecursive(root, result=[]):
    if not root:
        return
    inorderRecursive(root.left, result)
    result.append(root.data)
    inorderRecursive(root.right, result)
    return result


def run():
    root = BinaryTreeNode(1)
    node_left = BinaryTreeNode(2)
    node_right = BinaryTreeNode(3)

    root.left = node_left
    node_left.left = BinaryTreeNode(4)
    node_left.right = BinaryTreeNode(5)

    root.right = node_right
    node_right.left = BinaryTreeNode(6)
    node_right.right = BinaryTreeNode(7)

    print(root.getData())
    print(root.getLeft())
    print("preorderRecursive", preorderRecursive(node_left))
    print("inorderRecursive", inorderRecursive(root))

run()
