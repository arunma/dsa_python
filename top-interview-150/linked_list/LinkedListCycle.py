from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycle:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    node = ListNode(3)
    node.next = ListNode(2)
    node.next.next = ListNode(0)
    node.next.next.next = ListNode(-4)
    node.next.next.next.next = node.next
    init = LinkedListCycle()
    print(init.hasCycle(node))  # True

    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = node
    init = LinkedListCycle()
    print(init.hasCycle(node))  # True

    node = ListNode(1)
    init = LinkedListCycle()
    print(init.hasCycle(node))  # False
