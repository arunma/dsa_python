from collections import deque
from typing import *

from TreeNode import *


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = deque([])
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                self.values.append(node.val)
                node = node.right

    def next(self) -> int:
        return self.values.popleft()

    def hasNext(self) -> bool:
        return len(self.values) != 0


if __name__ == '__main__':
    init = BSTIterator(root=TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20))))
    print(init.next())  # 3
    print(init.next())  # 7
    print(init.hasNext())  # True
    print(init.next())  # 9
    print(init.hasNext())  # True
    print(init.next())  # 15
    print(init.hasNext())  # True
    print(init.next())  # 20
    print(init.hasNext())  # False
