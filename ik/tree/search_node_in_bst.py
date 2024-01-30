class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search_node_in_bst(root, value):
    if not root:
        return False
    if value == root.value:
        return True
    if value < root.value:
        return search_node_in_bst(root.left, value)
    else:
        return search_node_in_bst(root.right, value)


def search_node_in_bst(root, value):
    curr = root
    while curr:
        if value == curr.value:
            return True
        if value < curr.value:
            curr = curr.left
        else:
            curr = curr.right
    return False


if __name__ == '__main__':
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(4)
    root.right.right = BinaryTreeNode(6)
    print(search_node_in_bst(root, 4))
    print(search_node_in_bst(root, 7))
