from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedListCycleIISolution:
    def __init__(self, head: Optional[ListNode]):
        self.head: Optional[ListNode] = head

    def solve(self) -> Optional[ListNode]:

        if not self.head:
            return None

        fast_p, slow_p = self.head.next, self.head

        while fast_p and slow_p and fast_p != slow_p:
            fast_p = fast_p.next
            slow_p = slow_p.next

            if not fast_p:
                break
            fast_p = fast_p.next

        if not fast_p or not slow_p:
            return None

        cur_p = self.head

        while cur_p != fast_p:

            slow_p = fast_p

            while cur_p != slow_p and slow_p != fast_p:
                slow_p = slow_p.next

            if cur_p == slow_p:
                return cur_p
            cur_p = cur_p.next

        return cur_p

