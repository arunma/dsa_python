from typing import *

from leetcode.tree.treenode import TreeNode


class PostOrderTraversal:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        node = root
        while node or stack:
            if node:
                result.append(node.val)
                stack.append(node)
                node = node.right
            else:
                node = stack.pop()
                node = node.left

        return result[::-1]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def post_order(node, result):
            if node:
                post_order(node.left, result)
                post_order(node.right, result)
                result.append(node.val)

        result = []
        post_order(root, result)
        return result


if __name__ == '__main__':
    init = PostOrderTraversal()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    print(init.postorderTraversal(root=root))  # [3,2,1]
