from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DeleteMiddleNodeSolution:
    def __init__(self, head: Optional[ListNode]):

        self.head: Optional[ListNode] = head

    def solve(self) -> Optional[ListNode]:

        if self.head is None:
            return None

        if not self.head.next:
            return None

        fast_p, low_p = self.head.next, self.head

        while fast_p.next and fast_p.next.next:
            fast_p = fast_p.next.next
            low_p = low_p.next

        if low_p.next and low_p.next.next:
            low_p.next = low_p.next.next
        else:
            low_p.next = None

        return self.head


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


arr1 = [2,1]

head1 = init_linked_list(arr1)

sln = DeleteMiddleNodeSolution(head1)

print_linked_list(head1)
head1 = sln.solve()

print_linked_list(head1)