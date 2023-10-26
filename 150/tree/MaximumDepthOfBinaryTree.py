from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumDepthOfBinaryTree:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_depth = 1 + self.maxDepth(node.left)
        right_depth = 1 + self.maxDepth(node.right)
        return max(left_depth, right_depth)


if __name__ == '__main__':
    init = MaximumDepthOfBinaryTree()
    print(init.maxDepth(node=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # 3
    print(init.maxDepth(node=TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))  # 3
    print(init.maxDepth(node=TreeNode(0)))  # 1
    print(init.maxDepth(node=None))  # 0
