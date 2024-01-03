from typing import *

from TreeNode import *


class MinimumAbsoluteDifferenceInBST:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return sys.maxsize
        #
        # left_diff = abs(sys.maxsize if not root.left else root.left.val - root.val)
        # right_diff = abs(sys.maxsize if not root.right else root.right.val - root.val)
        #
        # left_side_diff = self.getMinimumDifference(root.left)
        # right_side_diff = self.getMinimumDifference(root.right)
        #
        # return min(left_diff, right_diff, left_side_diff, right_side_diff)

        node = root
        stack = []
        min_diff = float('inf')
        prev = float('inf')
        values = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                values.append(node.val)
                min_diff = min(min_diff, abs(node.val - prev))
                prev = node.val
                node = node.right
        return min_diff

        # def get_min_diff(node, low, high):
        #     if not node:
        #         return high - low
        #     left_diff = get_min_diff(node.left, low, node.val)
        #     right_diff = get_min_diff(node.right, node.val, high)
        #     return min(left_diff, right_diff)
        #
        # return get_min_diff(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    init = MinimumAbsoluteDifferenceInBST()
    # print(init.getMinimumDifference(root=TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))))  # 1
    # print(init.getMinimumDifference(root=TreeNode(4, TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)), TreeNode(6, None, None))))  # 1
    # print(init.getMinimumDifference(root=TreeNode(1, None, TreeNode(3, TreeNode(2, None, None), None))))  # 1
    print(init.getMinimumDifference(root=TreeNode(236, TreeNode(104, None, TreeNode(227)), TreeNode(701, None, TreeNode(911)))))  # 9
