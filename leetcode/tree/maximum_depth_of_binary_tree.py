from typing import Optional

from leetcode.tree.treenode import TreeNode


class MaximumDepthOfBinaryTree:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left = 1 + self.maxDepth(node.left)
        right = 1 + self.maxDepth(node.right)
        return max(left, right)

    # def height(self, node):
    #     return self.height_inner(node) - 1
    #
    # def height_inner(self, root):
    #     if not root:
    #         return 0
    #
    #     left = 1 + self.height_inner(root.left)
    #     right = 1 + self.height_inner(root.right)
    #     return max(left, right)


if __name__ == '__main__':
    init = MaximumDepthOfBinaryTree()
    print(init.maxDepth(node=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # 3
    # print(init.maxDepth(node=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # 3
    # print(init.maxDepth(node=TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))))  # 3
    # print(init.maxDepth(node=TreeNode(0)))  # 1
    # print(init.maxDepth(node=None))  # 0
