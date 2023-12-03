from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PathSum:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right and targetSum == root.val:
            return True

        if self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val):
            return True
        
        return False


if __name__ == '__main__':
    init = PathSum()
    print(init.hasPathSum(
        root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))),
        targetSum=22))  # True
    print(init.hasPathSum(root=TreeNode(1, TreeNode(2), TreeNode(3)), targetSum=5))  # False
    print(init.hasPathSum(root=TreeNode(1, TreeNode(2)), targetSum=0))  # False
