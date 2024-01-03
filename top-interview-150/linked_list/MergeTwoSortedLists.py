from typing import *

from LinkedList import *


class MergeTwoSortedLists:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        result = sent = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                result.next = ListNode(list1.val)
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                list2 = list2.next
            result = result.next
        if list1:
            result.next = list1
        if list2:
            result.next = list2

        return sent.next


if __name__ == '__main__':
    init = MergeTwoSortedLists()
    print(init.mergeTwoLists(list1=ListNode(1, ListNode(2, ListNode(4))), list2=ListNode(1, ListNode(3, ListNode(4)))))  # 1->1->2->3->4->4
    print(init.mergeTwoLists(list1=None, list2=None))  # None
    print(init.mergeTwoLists(list1=None, list2=ListNode(0)))  # 0
