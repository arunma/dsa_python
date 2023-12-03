from collections import deque
from typing import *

from TreeNode import *


class BinaryTreeRightSideView:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        queue = deque([root])
        result = []

        while queue:
            count = len(queue)
            for i in range(count):
                node = queue.popleft()
                if i == count - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


if __name__ == '__main__':
    init = BinaryTreeRightSideView()
    print(init.rightSideView(root=TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))  # [1, 3, 4])
    print(init.rightSideView(root=TreeNode(1, None, TreeNode(3))))  # [1, 3])
    print(init.rightSideView(root=None))  # [])
