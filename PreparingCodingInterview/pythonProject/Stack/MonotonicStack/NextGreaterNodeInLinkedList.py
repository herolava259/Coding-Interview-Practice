from typing import List, Optional, Deque as Stack, Tuple
from collections import deque as stack

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class NextLargeNodesSolution:
    def __init__(self, head: Optional[ListNode]):

        self.head: Optional[ListNode] = head

    def solve(self) -> List[int]:

        ans: List[int] = []

        cur_p: Optional = self.head
        p_idx: int = 0

        st: Stack[Tuple[int, int]] = stack()

        while cur_p:
            cur_v = cur_p.val

            while st and st[-1][1] < cur_v:
                prev_idx, _ = st.pop()
                ans[prev_idx] = cur_v
            st.append((p_idx, cur_v))
            ans.append(0)
            p_idx += 1
            cur_p = cur_p.next
        return ans

