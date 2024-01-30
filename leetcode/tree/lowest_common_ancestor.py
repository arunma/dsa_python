from treenode import TreeNode


class LowestCommonAncestor:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        queue = [root]
        while p not in parents or q not in parents:
            node = queue.pop(0)
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

        return None


if __name__ == '__main__':
    init = LowestCommonAncestor()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    print(init.lowestCommonAncestor(root, root.left, root.left.right.right))  # 5
    # print(init.lowestCommonAncestor(root, root.left, root.right))  # 3
