from typing import *

from TreeNode import *


class ConstructBinaryTreeFromInorderAndPostorderTraversal:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root_val = postorder.pop()
        root_index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)
        return root


if __name__ == '__main__':
    init = ConstructBinaryTreeFromInorderAndPostorderTraversal()
    print(init.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))  # [3,9,20,null,null,15,7]
    print(init.buildTree([-1], [-1]))  # [-1]
