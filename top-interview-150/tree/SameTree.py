from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SameTree:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    init = SameTree()
    print(init.isSameTree(p=TreeNode(1, TreeNode(2), TreeNode(3)), q=TreeNode(1, TreeNode(2), TreeNode(3))))  # True
    print(init.isSameTree(p=TreeNode(1, TreeNode(2)), q=TreeNode(1, None, TreeNode(2))))  # False
    print(init.isSameTree(p=TreeNode(1, TreeNode(2), TreeNode(1)), q=TreeNode(1, TreeNode(1), TreeNode(2))))  # False
