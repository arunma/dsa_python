from typing import *

from leetcode.tree.treenode import TreeNode


class MaximumWidthOfABinaryTree:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = float('-inf')
        queue = [(root, 1)]
        while queue:
            [print(n.val, pos) for n, pos in queue]
            level_width = queue[-1][1] - queue[0][1] + 1
            max_width = max(max_width, level_width)
            level_length = len(queue)
            for _ in range(level_length):
                node, pos = queue.pop(0)
                if node.left:
                    queue.append((node.left, pos * 2))
                if node.right:
                    queue.append((node.right, pos * 2 + 1))
        return max_width


if __name__ == '__main__':
    init = MaximumWidthOfABinaryTree()
    # print(init.widthOfBinaryTree(root=None))
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    print(init.widthOfBinaryTree(root=root))  # 4

    # root = TreeNode(1)
    # root.left = TreeNode(3)
    # root.left.left = TreeNode(5)
    # root.right = TreeNode(2)
    # print(init.widthOfBinaryTree(root=root))  # 2
