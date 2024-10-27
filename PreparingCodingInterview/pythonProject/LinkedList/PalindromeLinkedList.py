from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CheckPalindromeSolution:
    def __init__(self, head: Optional[ListNode]):

        self.head: Optional[ListNode] = head

    def solve(self) -> bool:

        if not self.head:
            return False

        st: List[ListNode] = [self.head]

        cur_p = self.head

        while cur_p.next:
            st.append(cur_p.next)
            cur_p = cur_p.next

        cur_p = self.head
        while st and cur_p:
            if st.pop().val != cur_p.val:
                return False

            cur_p = cur_p.next

        return True
