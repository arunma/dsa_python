from typing import *

from LinkedList import *


class RemoveNthNodeFromEndOfList:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n <= 0:
            return head

        fast = slow = head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    init = RemoveNthNodeFromEndOfList()
    print(init.removeNthFromEnd(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), n=2))  # 1->2->3->5->None
    print(init.removeNthFromEnd(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), n=5))  # 1->2->3->5->None
    print(init.removeNthFromEnd(head=ListNode(1), n=1))  # None
    print(init.removeNthFromEnd(head=ListNode(1, ListNode(2)), n=1))  # 1->None
