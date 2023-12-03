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


class BinaryTreeInorderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder_inner(node):
            if node and node.left:
                inorder_inner(node.left)
            if node:
                result.append(node.val)
            if node and node.right:
                inorder_inner(node.right)

        inorder_inner(root)
        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        result = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result


if __name__ == '__main__':
    init = BinaryTreeInorderTraversal()
    print(init.inorderTraversal(root=TreeNode(1, None, TreeNode(2, TreeNode(3)))))
    print(init.inorderTraversal(root=None))
    print(init.inorderTraversal(root=TreeNode(1)))
