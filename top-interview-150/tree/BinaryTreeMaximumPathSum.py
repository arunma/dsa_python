from typing import *

from TreeNode import *


class BinaryTreeMaximumPathSum:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0

        def max_path_sum(node) -> int:
            if not node:
                return 0
            lgain = max(max_path_sum(node.left), 0)
            rgain = max(max_path_sum(node.right), 0)
            curr_node_sum = node.val + lgain + rgain
            self.max_sum = max(self.max_sum, curr_node_sum)

            return node.val + max(lgain, rgain)

        max_path_sum(root)
        return self.max_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def max_path_sum(node) -> int:
            if not node:
                return 0

            lgain = max(max_path_sum(node.left), 0)
            rgain = max(max_path_sum(node.right), 0)
            node_sum = node.val + lgain + rgain

            nonlocal max_sum
            max_sum = max(max_sum, node_sum)

            return node.val + max(lgain, rgain)

        max_path_sum(root)
        return max_sum


if __name__ == '__main__':
    init = BinaryTreeMaximumPathSum()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(init.maxPathSum(root))

    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15, TreeNode(7))))
    print(init.maxPathSum(root))
