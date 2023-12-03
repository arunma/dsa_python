from collections import deque
from typing import *

from TreeNode import *


class AverageOfLevelsInBinaryTree:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []
        while queue:
            count = len(queue)
            sum = 0
            for _ in range(count):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sum += node.val
            result.append(sum / count)
        return result


if __name__ == '__main__':
    init = AverageOfLevelsInBinaryTree()
    print(init.averageOfLevels(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))  # [3, 14.5, 11])
    print(init.averageOfLevels(root=TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))))  # [3, 14.5, 11])
