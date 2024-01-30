from typing import *


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


class ConstructBinarySearchTreeToSortedDoublyLinkedList:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = sent = Node(0)
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                head.right, node.left = node, head
                head = head.right
                node = node.right
        sent.right.left, head.right = head, sent.right
        return sent.right


if __name__ == '__main__':
    init = ConstructBinarySearchTreeToSortedDoublyLinkedList()
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    print(init.treeToDoublyList(root))  # 1 <-> 2 <-> 3 <-> 4 <-> 5
