from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class OddEvenListSolution:

    def __init__(self, head: Optional[ListNode]):
        self.head: Optional[ListNode] = head

    def solve(self) -> Optional[ListNode]:
        if not self.head:
            return None

        odd_p = self.head
        even_head_p = ListNode()
        prev_odd_p = self.head
        even_p = even_head_p
        while odd_p and odd_p.next:
            even_p.next = odd_p.next
            odd_p.next = odd_p.next.next
            prev_odd_p = odd_p
            odd_p = odd_p.next
            even_p = even_p.next
            even_p.next = None

        if not odd_p:
            prev_odd_p.next = even_head_p.next
        else:
            odd_p.next = even_head_p.next

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


arr1 = [2,1,3,5,6,4,7]

head1 = init_linked_list(arr1)

sln = OddEvenListSolution(head1)

head1 = sln.solve()

print_linked_list(head1)
