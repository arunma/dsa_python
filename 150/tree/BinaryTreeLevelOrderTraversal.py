from collections import deque
from typing import *

from TreeNode import *


class BinaryTreeLevelOrderTraversal:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            count = len(queue)
            level = []
            for _ in range(count):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


if __name__ == '__main__':
    init = BinaryTreeLevelOrderTraversal()
    print(init.levelOrder(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # [[3],[9,20],[15,7]])
    print(init.levelOrder(root=TreeNode(1)))  # [[1]])
    print(init.levelOrder(root=None))  # [])
