from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return merge_sort(head)


def merge_sort(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    if not head.next:
        return head
    by_p = ListNode(0, head)
    slow_p = by_p
    fast_p = by_p
    while fast_p.next and fast_p.next.next:
        fast_p = fast_p.next.next
        slow_p = slow_p.next

    nxt_head = slow_p.next
    slow_p.next = None
    head = merge_sort(head)
    next_head = merge_sort(nxt_head)

    new_head = merge(head, next_head)
    return new_head


def merge(head1: Optional[ListNode], head2: Optional[ListNode]) -> ListNode | None:
    head = ListNode()
    cur_p = head
    p1, p2 = head1, head2
    while p1 and p2:
        if p1.val <= p2.val:
            cur_p.next = p1
            p1 = p1.next
        else:
            cur_p.next = p2
            p2 = p2.next
        cur_p = cur_p.next
        cur_p.next = None
    if p1:
        cur_p.next = p1
    if p2:
        cur_p.next = p2

    return head.next


arr1 = [4, 2, 1, 3]

head1 = ListNode(arr1[0])
cur_p = head1
for e in arr1[1:]:
    cur_p.next = ListNode(e)
    cur_p = cur_p.next

sln = Solution()

res1 = sln.sortList(head1)

while res1:
    print(res1.val)
    res1 = res1.next
