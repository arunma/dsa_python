from treenode import BinaryTreeNode


def inorder(node, result):
    if not node:
        return None
    else:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)


def merge_two_binary_search_trees(root1, root2):
    root1_inorder, root2_inorder = [], []
    inorder(root1, root1_inorder)
    inorder(root2, root2_inorder)

    merged = sorted(root1_inorder + root2_inorder)

    return array_to_bst(merged, 0, len(merged) - 1)


def array_to_bst(array, low, high):
    if low > high:
        return None
    mid = low + (high - low) // 2
    root = BinaryTreeNode(array[mid])
    root.left = array_to_bst(array, low, mid - 1)
    root.right = array_to_bst(array, mid + 1, high)
    return root


if __name__ == '__main__':
    root1 = BinaryTreeNode(5)
    root1.left = BinaryTreeNode(3)
    root1.right = BinaryTreeNode(6)
    root1.left.left = BinaryTreeNode(2)
    root1.left.right = BinaryTreeNode(4)
    root1.right.right = BinaryTreeNode(7)

    root2 = BinaryTreeNode(8)
    root2.left = BinaryTreeNode(1)
    root2.right = BinaryTreeNode(9)
    print(merge_two_binary_search_trees(root1, root2))
