from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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


class PopulatingNextRightPointersInEachNodeII:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque([root])

        while queue:
            level_count = len(queue)
            prev = None
            for _ in range(level_count):
                node = queue.popleft()
                if prev:
                    prev.next = node
                prev = node

                # add next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


if __name__ == '__main__':
    init = PopulatingNextRightPointersInEachNodeII()
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
    print(init.connect(root))
