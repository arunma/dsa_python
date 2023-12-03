from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PreorderTraversal:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        result = []
        while node or stack:
            if node:
                result.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        return result


if __name__ == '__main__':
    init = PreorderTraversal()
    print(init.preorderTraversal(root=TreeNode(1, None, TreeNode(2, TreeNode(3)))))  # [1, 2, 3])
    print(init.preorderTraversal(root=TreeNode(1, TreeNode(2))))  # [1, 2])
    print(init.preorderTraversal(root=TreeNode(1, None, TreeNode(2))))  # [1, 2])
    print(init.preorderTraversal(root=None))  # [])
    print(init.preorderTraversal(root=TreeNode(1)))
