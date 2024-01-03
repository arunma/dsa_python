from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreePostorderTraversal:
    # def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     stack = []
    #     node = root
    #     result = []
    #     while node or stack:
    #         if node:
    #             result.append(node.val)
    #             stack.append(node)
    #             node = node.right
    #         else:
    #             node = stack.pop()
    #             node = node.left
    #     return result[::-1]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        node = root
        while node or stack:
            if node:
                result.append(node.val)
                stack.append(node.left)
                node = node.right
            else:
                node = stack.pop()
        return result[::-1]


if __name__ == '__main__':
    init = BinaryTreePostorderTraversal()
    print(init.postorderTraversal(root=TreeNode(1, None, TreeNode(2, TreeNode(3)))))  # [3, 2, 1])
    print(init.postorderTraversal(root=TreeNode(1, TreeNode(2))))  # [2, 1])

    root = TreeNode(5)
    root.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.right = TreeNode(6)

    print(init.postorderTraversal(root))
