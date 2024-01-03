from typing import *

from TreeNode import *


class PathSumII:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.path_sum(root, targetSum, [], result)
        return result

    def path_sum(self, node, target, path, result):
        if not node:
            return
        if not node.left and not node.right and target == node.val:
            result.append(path + [node.val])
            return

        self.path_sum(node.left, target - node.val, path + [node.val], result)
        self.path_sum(node.right, target - node.val, path + [node.val], result)


if __name__ == '__main__':
    init = PathSumII()
    print(
        init.pathSum(
            root=TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),
            targetSum=22))  # [[5,4,11,2],[5,8,4,5]])
    print(init.pathSum(root=TreeNode(1, TreeNode(2), TreeNode(3)), targetSum=5))  # [])
    print(init.pathSum(root=TreeNode(1, TreeNode(2)), targetSum=0))  # [])
