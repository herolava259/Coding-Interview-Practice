from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def reverse_linked_list(first_p: ListNode, second_p: ListNode) -> ListNode:
    third_p = second_p.next
    second_p.next = first_p
    if not third_p:
        return second_p
    return reverse_linked_list(second_p, third_p)


class ReverseLinkedList:
    def __init__(self, head: Optional[ListNode]):
        self.head: Optional[ListNode] = head

    def solve(self) -> Optional[ListNode]:
        if not self.head or not self.head.next:
            return self.head
        first_p = self.head
        second_p = first_p.next
        first_p.next = None
        return reverse_linked_list(first_p, second_p)


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


arr1 = []

head1 = init_linked_list(arr1)

sln = ReverseLinkedList(head1)

head1 = sln.solve()

print_linked_list(head1)
