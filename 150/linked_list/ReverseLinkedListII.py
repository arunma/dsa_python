from typing import *

from LinkedList import *


class ReverseLinkedListII:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        left_node_prev = None
        right_node_next = None

        count = 0
        node = head
        while node:
            count += 1
            if count == left - 1:
                left_node_prev = node
            elif count == right + 1:
                right_node_next = node
            node = node.next

        prev = None
        left_node = node = left_node_prev.next

        while node and node != right_node_next:
            next = node.next
            node.next = prev
            prev = node
            node = next

        left_node_prev.next = prev
        left_node.next = right_node_next

        return head

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        sent = prev = ListNode(0, head)
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return sent.next


if __name__ == '__main__':
    init = ReverseLinkedListII()
    print(init.reverseBetween(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), left=2, right=4))  # 1->4->3->2->5->None
    print(init.reverseBetween(head=ListNode(5), left=1, right=1))  # 5->None
