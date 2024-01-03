from typing import *


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        return str(self.val) + "->" + (str(self.next) if self.next else "")


class CopyListWithRandomPointer:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        copy = {}
        node = head
        while node:
            copy[node] = Node(node.val, None)
            node = node.next

        node = head
        result = sent = Node(0)
        while node:
            result.next = copy[node]
            if node.next:
                result.next.next = copy[node.next]
            if node.random:
                result.next.random = copy[node.random]
            node = node.next
            result = result.next
        return sent.next


if __name__ == '__main__':
    init = CopyListWithRandomPointer()
    seven = Node(7)
    thirteen = Node(13)
    eleven = Node(11)
    ten = Node(10)
    one = Node(1)
    seven.next = thirteen
    thirteen.next = eleven
    eleven.next = ten
    ten.next = one
    seven.random = None
    thirteen.random = seven
    eleven.random = one
    ten.random = eleven
    one.random = seven
    print(init.copyRandomList(seven))  # 7->13->11->10->1

    init = CopyListWithRandomPointer()
    one = Node(1)
    two = Node(2)
    one.next = two
    one.random = two
    two.random = two
    print(init.copyRandomList(one))  # 1->2
