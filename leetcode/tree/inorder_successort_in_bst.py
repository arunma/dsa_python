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


class InorderSuccessortInBst:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None

        if p.right:
            curr = p.right
            while curr.left:
                curr = curr.left
            return curr

        ancestor = None
        curr = root

        while curr.val != p.val:
            if p.val < curr.val:
                ancestor = curr
                curr = curr.left
            else:
                curr = curr.right
        return ancestor

        #
        # if not root:
        #     return None
        #
        # if p.val >= root.val:
        #     return self.inorderSuccessor(root.right, p)
        # else:
        #     left = self.inorderSuccessor(root.left, p)
        #     return left if left else root


if __name__ == '__main__':
    init = InorderSuccessortInBst()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(init.inorderSuccessor(root, root.left))  # 2

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    print(init.inorderSuccessor(root, root.right))  # None
