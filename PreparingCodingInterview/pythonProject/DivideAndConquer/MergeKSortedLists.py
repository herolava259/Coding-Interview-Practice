from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MergeKSortedListSolution:

    def __init__(self, lists: List[Optional[ListNode]]):
        self.lists: List[Optional[ListNode]] = lists

    def solve(self) -> Optional[ListNode]:
        return self.divide_and_merge(0, len(self.lists) - 1)

    def divide_and_merge(self, beg_idx, end_idx) -> Optional[ListNode]:
        if beg_idx == end_idx:
            return self.lists[beg_idx]

        split_idx = (beg_idx + end_idx) // 2

        first_p = self.divide_and_merge(beg_idx, split_idx)
        second_p = self.divide_and_merge(split_idx + 1, end_idx)

        by_p = ListNode(-1)
        cur_p = by_p
        cur_p1, cur_p2 = first_p, second_p

        while cur_p1 and cur_p2:
            if cur_p1.val <= cur_p2.val:
                cur_p.next = cur_p1
                cur_p1 = cur_p1.next
            else:
                cur_p.next = cur_p2
                cur_p2 = cur_p2.next

            cur_p = cur_p.next
            cur_p.next = None

        if cur_p1:
            cur_p.next = cur_p1
        elif cur_p2:
            cur_p.next = cur_p2

        return by_p.next
