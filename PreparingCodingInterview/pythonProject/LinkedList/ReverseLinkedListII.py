from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, nxt: Optional['ListNode'] = None):
        self.val = val
        self.next: Optional['ListNode'] = nxt


def reverse_linked_list(head: ListNode):

    cur_p = head
    nxt_p = cur_p.next

    while nxt_p is not None:

        tmp_p = nxt_p.next
        nxt_p.next = cur_p
        cur_p = nxt_p
        nxt_p = tmp_p

    return nxt_p


class ReverseLinkedListIISolution:

    def __init__(self, head: Optional[ListNode], left: int, right: int):
        self.head: Optional[ListNode] = ListNode(-1, head)
        self.left: int = left
        self.right: int = right

    def solve(self) -> Optional[ListNode]:

        if self.head.next is None:
            return self.head.next
        if self.left == self.right:
            return self.head.next

        prev_left: ListNode | None = self.find_cur_p(self.left-1)
        cur_right: ListNode | None = self.find_cur_p(self.right)

        if cur_right is None or prev_left is None:
            return self.head.next
        nxt_right = cur_right.next
        cur_right.next = None

        cur_left = prev_left.next

        reverse_linked_list(cur_left)

        cur_left.next = nxt_right
        prev_left.next = cur_right

        return self.head.next

    def find_cur_p(self, pos: int) -> Optional[ListNode]:

        counter = 0
        cur_p = self.head
        while cur_p and counter < pos:
            cur_p = cur_p.next
            counter += 1

        return cur_p

    def find_prev_p(self, val: int) -> Optional[ListNode]:

        cur_p: ListNode = self.head.next
        if cur_p is None:
            return cur_p
        if cur_p.val == val:
            return self.head

        while cur_p.next is not None and cur_p.next.val != val:
            cur_p = cur_p.next

        if cur_p.next is None:
            return cur_p.next
        return cur_p

    def find_last_p(self, val: int) -> Optional[List]:

        cur_p: ListNode = self.head.next

        if cur_p is None:
            return cur_p

        while cur_p and cur_p.val != val:
            cur_p = cur_p.next

        if cur_p is None:
            return cur_p

        while cur_p.next and cur_p.next.val == val:
            cur_p = cur_p.next

        return cur_p



