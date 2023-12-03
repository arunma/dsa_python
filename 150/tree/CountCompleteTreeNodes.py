from collections import deque
from typing import *

from TreeNode import *


class CountCompleteTreeNodes:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])

        count = 0
        while queue:
            curr_len = len(queue)
            count += curr_len
            for _ in range(curr_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return count


if __name__ == '__main__':
    init = CountCompleteTreeNodes()
    print(init.countNodes(root=TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))  # 6
