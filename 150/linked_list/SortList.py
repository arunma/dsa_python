from typing import *

from LinkedList import *


class SortList:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        left = head
        right = slow.next
        slow.next = None

        sleft = self.sortList(left)
        sright = self.sortList(right)
        merged = self.mergeLists(sleft, sright)
        return merged

    def mergeLists(self, left, right) -> Optional[ListNode]:
        if not left and not right:
            return None
        sent = head = ListNode(0)
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        head.next = left or right
        return sent.next


if __name__ == '__main__':
    init = SortList()
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
    print(init.sortList(head))
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    print(init.sortList(head))
