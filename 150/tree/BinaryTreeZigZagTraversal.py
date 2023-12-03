from collections import deque
from typing import *

from TreeNode import *


class BinaryTreeZigZagTraversal:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []
        left_to_right = True
        while queue:
            count = len(queue)
            level = deque([])
            for _ in range(count):
                node = queue.popleft()
                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            left_to_right = not left_to_right
            result.append(level)
        return result


if __name__ == '__main__':
    init = BinaryTreeZigZagTraversal()
    print(init.zigzagLevelOrder(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # [[3],[20,9],[15,7]])
    print(init.zigzagLevelOrder(root=TreeNode(1)))  # [[1]])
    print(init.zigzagLevelOrder(root=None))  # [])
