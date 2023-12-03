from typing import *

from TreeNode import *


class ValidateBinarySearchTree:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.is_valid_bst(root, float('-inf'), float('inf'))

    def is_valid_bst(self, node, lmax, rmax):
        if not node:
            return True
        if not lmax < node.val < rmax:
            return False
        return self.is_valid_bst(node.left, lmax, node.val) and self.is_valid_bst(node.right, node.val, rmax)


if __name__ == '__main__':
    init = ValidateBinarySearchTree()
    print(init.isValidBST(root=TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))))  # True
    print(init.isValidBST(root=TreeNode(5, TreeNode(1, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None)))))  # False
