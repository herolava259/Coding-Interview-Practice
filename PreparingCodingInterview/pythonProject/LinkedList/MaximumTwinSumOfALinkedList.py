from typing import List, Optional, Deque
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MaxPairSumSolution:
    def __init__(self, head: Optional[ListNode]):
        self.head: Optional[ListNode] = head

    def solve(self) -> int:

        if not self.head:
            return 0

        n = 0
        st: Deque[ListNode] = deque()

        cur_p: ListNode = self.head

        while cur_p:
            st.append(cur_p)
            n += 1
            cur_p = cur_p.next
        cur_p = self.head
        max_pair_sum = 0
        for i in range(n // 2):
            tmp_sum = cur_p.val + st.pop().val
            if tmp_sum > max_pair_sum:
                max_pair_sum = tmp_sum
            cur_p = cur_p.next

        return max_pair_sum


def init_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None

    head = ListNode(arr[0])
    cur_p = head

    for item in arr[1:]:
        cur_p.next = ListNode(item, None)
        cur_p = cur_p.next

    return head


def print_linked_list(head: Optional[ListNode]):
    if not head:
        return

    cur_p = head.next
    print_str = str(head.val)
    while cur_p:
        print_str += f' -> {cur_p.val}'
        cur_p = cur_p.next

    print(print_str)

arr = [5,4,2,1]

head1 = init_linked_list(arr)

sln = MaxPairSumSolution(head1)

print(sln.solve())