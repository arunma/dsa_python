from typing import *

from LinkedList import *


class AddTwoNumbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = sent = ListNode(0)

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, rem = divmod(carry, 10)
            result.next = ListNode(rem)
            result = result.next
        return sent.next


if __name__ == '__main__':
    init = AddTwoNumbers()
    print(init.addTwoNumbers(l1=ListNode(2, ListNode(4, ListNode(3))), l2=ListNode(5, ListNode(6, ListNode(4)))))  # 7->0->8
    print(init.addTwoNumbers(l1=ListNode(0), l2=ListNode(0)))  # 0
    print(init.addTwoNumbers(l1=ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
                             l2=ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))  # 8->9->9->9->0->0->0->1
