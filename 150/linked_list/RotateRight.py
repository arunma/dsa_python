from typing import *

from LinkedList import *


class RotateRight:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == 1:
            return head
        elif k % length == 0:
            return head
        elif k > length:
            k = k % length

        fast = prev = head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            fast = fast.next
            prev = prev.next

        new_begin = prev.next
        prev.next = None

        fast.next = head

        return new_begin


if __name__ == '__main__':
    init = RotateRight()
    print(init.rotateRight(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), k=2))  # 4->5->1->2->3->None
    # print(init.rotateRight(head=ListNode(0, ListNode(1, ListNode(2))), k=4))  # 2->0->1->None
    print(init.rotateRight(head=ListNode(1), k=1))  # [1]
    print(init.rotateRight(head=ListNode(1), k=99))  # [1]
    print(init.rotateRight(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), k=10))
