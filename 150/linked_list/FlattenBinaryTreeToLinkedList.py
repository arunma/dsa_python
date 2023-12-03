from collections import deque
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, depth=5):
        ret = ""

        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)

        # Print own value
        ret += "\n" + ("    " * depth) + str(self.val)

        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)

        return ret


class FlattenBinaryTreeToLinkedList:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None
        stack = []
        node = root
        nodes = deque([])

        while node or stack:
            if node:
                nodes.append(node)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()

        root = nodes.popleft()
        while nodes:
            root.right = nodes.popleft()
            root.left = None
            root = root.right

    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right


if __name__ == '__main__':
    init = FlattenBinaryTreeToLinkedList()
    print(init.flatten(root=TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)))))
    print(init.flatten(root=TreeNode(1, TreeNode(2, None, TreeNode(3, None, None)), TreeNode(2, None, TreeNode(3, None, None)))))
    print(init.flatten(root=TreeNode(1, TreeNode(2, None, None), TreeNode(2, None, None))))
    print(init.flatten(root=TreeNode(0)))
    print(init.flatten(root=None))
