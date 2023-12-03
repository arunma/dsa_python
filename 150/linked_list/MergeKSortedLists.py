import heapq
from typing import *

from LinkedList import *


class MergeKSortedLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        pq = []
        for i, each in enumerate(lists):
            if each:
                heapq.heappush(pq, (each.val, i, each))

        sent = head = ListNode(0)
        while pq:
            top_val, i, top = heapq.heappop(pq)
            head.next = ListNode(top_val)
            head = head.next
            if top.next:
                heapq.heappush(pq, (top.next.val, i, top.next))

        return sent.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        one, two = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge_two_lists(one, two)

    def merge_two_lists(self, left, right):
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
    init = MergeKSortedLists()
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    print(init.mergeKLists(lists))
    lists = []
    print(init.mergeKLists(lists))
    lists = [[]]
    print(init.mergeKLists(lists))
