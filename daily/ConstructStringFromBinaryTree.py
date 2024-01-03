from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ConstructStringFromBinaryTree:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ''

        result = str(root.val)
        if root.left:
            result += '(' + self.tree2str(root.left) + ')'

        if not root.left and root.right:
            result += '()'

        if root.right:
            result += '(' + self.tree2str(root.right) + ')'
        return result


if __name__ == '__main__':
    init = ConstructStringFromBinaryTree()
    one = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    print(init.tree2str(one))  # "1(2(4))(3)"
    two = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    print(init.tree2str(two))  # "1(2()(4))(3)"
    three = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5)))
    print(init.tree2str(three))  # "1(2(4))(3(5))"
