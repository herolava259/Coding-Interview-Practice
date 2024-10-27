from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class GetIntersectionNodeSolution:
    def __init__(self, headA: ListNode, headB: ListNode):
        self.headA: ListNode = headA
        self.headB: ListNode = headB

    def solve(self) -> Optional[ListNode]:

        cur_pa = self.headA

        prev_p_dict = dict()

        while cur_pa:
            prev_p_dict[cur_pa] = True
            cur_pa = cur_pa.next

        cur_pb = self.headB

        while cur_pb:

            if prev_p_dict.get(cur_pb, False):
                return cur_pb

            cur_pb = cur_pb.next

        return None
