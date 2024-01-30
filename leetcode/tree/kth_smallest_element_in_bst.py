class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def kth_smallest_element(root, k):
    node = root
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if k == 1:
                return node.value
            else:
                k -= 1
            node = node.right
    return -1


if __name__ == '__main__':
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(3)
    print(kth_smallest_element(root, 3))
