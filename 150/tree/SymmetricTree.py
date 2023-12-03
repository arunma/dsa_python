from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SymmetricTree:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.isSymmetricLR(root.left, root.right):
            return True
        return False

    def isSymmetricLR(self, left, right) -> bool:
        if not left and not right:
            return True
        elif left and right and left.val == right.val and self.isSymmetricLR(left.left, right.right) and self.isSymmetricLR(left.right, right.left):
            return True
        return False


if __name__ == '__main__':
    init = SymmetricTree()
    print(init.isSymmetric(root=TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)),
                                         TreeNode(2, TreeNode(4, None, None), TreeNode(3, None, None)))))  # True
    print(init.isSymmetric(root=TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(2, None, TreeNode(3, None, None)))))  # False
    print(init.isSymmetric(root=TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))))  # True
