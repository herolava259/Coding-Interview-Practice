from typing import List, Optional, Deque
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class ReorderListSolution:
    def __init__(self, head: Optional[ListNode]):
        self.head: Optional[ListNode] = head

    def solve(self) -> None:
        if not self.head:
            return

        q: Deque[ListNode] = deque()

        virtual_p = ListNode(0, self.head)
        cur_p = self.head

        q.append(cur_p)
        while cur_p.next:
            q.append(cur_p.next)
            cur_p = cur_p.next
        cur_p = virtual_p
        while len(q) >1:
            cur_p.next = q.popleft()
            cur_p = cur_p.next
            cur_p.next = q.pop()
            cur_p = cur_p.next

        if not q:
            cur_p.next = q.pop()
            cur_p = cur_p.next
        
        cur_p.next = None


