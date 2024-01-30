from typing import *

from treenode import TreeNode


class BinaryTreePaths:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, curr):
        if not node:
            return

        curr.append(str(node.val))
        if not node.left and not node.right:
            result.append('->'.join(curr))
            return

        self.dfs(node.left, result, curr)
        self.dfs(node.right, result, curr)
        curr.pop()

    # def dfs1(self, node, result, path):
    #     if not node:
    #         return
    #
    #     path.append(str(node.val))
    #     if not node.left and not node.right:
    #         result.append('->'.join(path))
    #
    #     self.dfs(node.left, result, path)
    #     self.dfs(node.right, result, path)
    #     path.pop()


if __name__ == '__main__':
    init = BinaryTreePaths()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    print(init.binaryTreePaths(root))
