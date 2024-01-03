from collections import deque
from typing import *

from TreeNode import *


class ConstructBinaryTreeFromPreorderAndInorderTraversal:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        root = self.buildTreeInner(preorder, inorder)
        return root

    def buildTreeInner(self, preorder: deque[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        root_val = preorder.popleft()
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTreeInner(preorder, inorder[:root_index])
        root.right = self.buildTreeInner(preorder, inorder[root_index + 1:])
        return root


if __name__ == '__main__':
    init = ConstructBinaryTreeFromPreorderAndInorderTraversal()
    print(init.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]))  # [3,9,20,null,null,15,7]
    print(init.buildTree(preorder=[-1], inorder=[-1]))  # [-1]
