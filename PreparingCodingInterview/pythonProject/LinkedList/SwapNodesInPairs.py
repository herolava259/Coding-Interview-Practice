from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SwapNodesInPairSolution:

    def __init__(self, head: Optional[ListNode]):
        self.head: Optional[ListNode] = head

    def solve(self) -> Optional[ListNode]:

        if not self.head:
            return None

        by_p: ListNode = ListNode(0,self.head)

        head_p = by_p
        first_p = self.head
        second_p = first_p.next

        while first_p and second_p:

            first_p.next = second_p.next
            head_p.next = second_p
            second_p.next = first_p
            head_p = first_p
            first_p, second_p = None, None

            if head_p.next:
                first_p = head_p.next
            if first_p:
                second_p = first_p.next

        return by_p.next


