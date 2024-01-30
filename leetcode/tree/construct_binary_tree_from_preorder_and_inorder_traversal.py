from typing import *

from treenode import TreeNode


class ConstructBinaryTreeFromPreorderAndInorderTraversal:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build_tree(preorder, inorder)

    def build_tree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        rv = preorder.pop(0)
        ri = inorder.index(rv)
        root = TreeNode(rv)
        root.left = self.build_tree(preorder, inorder[:ri])
        root.right = self.build_tree(preorder, inorder[ri + 1:])
        return root


if __name__ == '__main__':
    init = ConstructBinaryTreeFromPreorderAndInorderTraversal()
    print(init.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))  # [3, 9, 20, 15, 7])
    print(init.buildTree(preorder=[-1], inorder=[-1]))  # [-1])
