from collections import deque

from TreeNode import *


class LowestCommonAncestorOfBinaryTree:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        queue = deque([root])

        while p not in parents or q not in parents:
            node = queue.popleft()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)

        pparents = set()
        while p:
            pparents.add(p)
            p = parents[p]

        while q:
            if q in pparents:
                return q
            q = parents[q]

        return root


if __name__ == '__main__':
    init = LowestCommonAncestorOfBinaryTree()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    print(init.lowestCommonAncestor(root, root.left, root.right))  # 3

    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    print(init.lowestCommonAncestor(root, root.left, root.left.right.right))  # 5
    root = TreeNode(1, TreeNode(2))
    print(init.lowestCommonAncestor(root, root, root.left))  # 1
