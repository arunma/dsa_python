"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def inorder(node, result):
    if node:
        inorder(node.left, result)
        result.append(node.value)
        inorder(node.right, result)


def merge_two_binary_search_trees(root1, root2):
    result1, result2 = [], []
    inorder(root1, result1)
    inorder(root2, result2)

    merged = sorted(result1 + result2)

    return build_bst_from_array(merged, 0, len(merged) - 1)


def build_bst_from_array(arr, low, high):
    if low > high:
        return None

    mid = low + (high - low) // 2
    root = BinaryTreeNode(arr[mid])
    root.left = build_bst_from_array(arr, low, mid - 1)
    root.right = build_bst_from_array(arr, mid + 1, high)

    return root
