from typing import *

from LinkedList import *


class ReverseLinkedList:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev


if __name__ == '__main__':
    init = ReverseLinkedList()
    print(init.reverseList(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))  # 5->4->3->2->1->None
    print(init.reverseList(head=ListNode(1, ListNode(2))))  # 2->1->None
