class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    node = root
    stack = []
    result = []
    while node or stack:
        if node:
            result.append(node.value)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right

    return result


if __name__ == '__main__':
    root = BinaryTreeNode(0)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(4)
    print(preorder(root))
