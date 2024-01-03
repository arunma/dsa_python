from typing import *

from LinkedList import *


class PartitionList:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = left_sent = ListNode(0, None)
        right = right_sent = ListNode(0, None)
        node = head
        while node:
            if node.val < x:
                left.next = node  # ListNode(node.val, None)
                left = left.next
            else:
                right.next = node  # ListNode(node.val, None)
                right = right.next
            node = node.next

        right.next = None
        left.next = right_sent.next
        return left_sent.next


if __name__ == '__main__':
    init = PartitionList()
    print(init.partition(head=ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), x=3))  # 1->2->2->4->3->5->None
    print(init.partition(head=ListNode(2, ListNode(1)), x=2))  # 1->2->None
