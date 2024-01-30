from collections import defaultdict
from typing import *

from treenode import TreeNode


class VerticalOrderTraversalOfABinaryTree:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        result = defaultdict(list)

        while queue:
            level = len(queue)
            level_list = defaultdict(list)
            for _ in range(level):
                node, pos = queue.pop(0)
                # result[pos].append(node.val)
                level_list[pos].append(node.val)
                if node.left:
                    queue.append((node.left, pos - 1))
                if node.right:
                    queue.append((node.right, pos + 1))
            for pos, nl in level_list.items():
                result[pos].extend(sorted(nl))

        return [result[pos] for pos in sorted(result.keys())]


if __name__ == '__main__':
    init = VerticalOrderTraversalOfABinaryTree()
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.right = TreeNode(3)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(5)
    # root.right.left = TreeNode(6)
    # root.right.right = TreeNode(7)
    # print(init.verticalTraversal(root))  # [[4],[2],[1,5,6],[3],[7]]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(init.verticalTraversal(root))  # [[4],[2],[1,6,5],[3],[7]]
