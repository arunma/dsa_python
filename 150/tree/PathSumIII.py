from collections import defaultdict
from typing import *

from TreeNode import *


class PathSumIII:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def preorder(node, curr_sum):
            if not node:
                return
            curr_sum += node.val
            nonlocal count
            count += prefix_sum[curr_sum - targetSum]
            prefix_sum[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            prefix_sum[curr_sum] -= 1

        count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        preorder(root, 0)
        return count


if __name__ == '__main__':
    init = PathSumIII()
    print(init.pathSum(
        TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11))), 8))  # 3
    # print(init.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))),
    #                    22))  # 2
    # print(init.pathSum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))  # 0
    # print(init.pathSum(TreeNode(1, TreeNode(2)), 0))  # 0
    # print(init.pathSum(TreeNode(1, TreeNode(-2), TreeNode(-3)), -1))  # 1
