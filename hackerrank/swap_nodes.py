from leetcode.tree.treenode import TreeNode


def inorder_traversal(root, result):
    if not root:
        return None
    inorder_traversal(root.left, result)
    result.append(root.val)
    inorder_traversal(root.right, result)


def swap_nodes(node, k):
    root = node
    result = []
    inorder_traversal(root, result)
    print(result)
    swap_nodes_inner(node, k, 1)
    result = []
    inorder_traversal(root, result)
    print(result)


def swap_nodes_inner(node, k, level):
    if not node:
        return
    if k == level:
        node.left, node.right = node.right, node.left
    swap_nodes_inner(node.left, k, level + 1)
    swap_nodes_inner(node.right, k, level + 1)


if __name__ == '__main__':
    tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    print(swap_nodes(tree, 2))
    # tree = TreeNode(2, TreeNode(1), TreeNode(3))
    # print(swap_nodes(tree, 2))
