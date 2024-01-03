from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumRootToLeafNumbers:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        self.sumNumbersInner(root, str(root.val), result)
        return sum(result)

    def sumNumbersInner(self, node, curr, result):
        if not node:
            return

        if not node.left and not node.right:
            result.append(int(curr))
            return

        if node.left:
            self.sumNumbersInner(node.left, curr + str(node.left.val), result)
        if node.right:
            self.sumNumbersInner(node.right, curr + str(node.right.val), result)


if __name__ == '__main__':
    init = SumRootToLeafNumbers()
    print(init.sumNumbers(root=TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))))  # 25
    print(init.sumNumbers(root=TreeNode(4, TreeNode(9, TreeNode(5, None, None), TreeNode(1, None, None)), TreeNode(0, None, None))))  # 1026
