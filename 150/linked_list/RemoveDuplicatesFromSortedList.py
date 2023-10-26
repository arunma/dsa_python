from typing import *

from LinkedList import *


class RemoveDuplicatesFromSortedList:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = sent = ListNode(0, head)
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next

            if prev.next == curr:
                prev = prev.next
                curr = curr.next
            else:
                prev.next = curr.next
                curr = curr.next
        return sent.next


if __name__ == '__main__':
    init = RemoveDuplicatesFromSortedList()
    print(init.deleteDuplicates(head=ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))))  # 1->2->5->None
    # print(init.deleteDuplicates(head=ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3)))))))  # 2->3->None
