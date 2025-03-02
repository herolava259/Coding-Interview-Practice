from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ReverseKGroupSolution:
    def __init__(self, head: Optional[ListNode], k: int):
        self.head: Optional[ListNode] = head
        self.k: int = k

    def solve(self) -> Optional[ListNode]:
        n = 0
        cur_p = self.head
        while cur_p:
            n+=1
            cur_p = cur_p.next

        num_step = n // self.k
        return reverse(self.head, self.k, num_step)


def reverse(cur_node: Optional[ListNode], k,num_step = 0) -> Optional[ListNode]:
    if not cur_node:
        return None
    if num_step == 0:
        return cur_node
    head_p: ListNode = cur_node

    counter = 1
    cur_p = head_p
    prev_p: Optional[ListNode] = None
    while cur_p and counter <= k:
        nxt_p = cur_p.next
        cur_p.next = prev_p
        prev_p = cur_p
        cur_p = nxt_p
        counter += 1
    if cur_p is None:
        return prev_p

    head_p.next = reverse(cur_p, k, num_step-1)

    return prev_p

test1 = [1,2,3,4,5]

root = ListNode(test1[0])
cur_pp = root
for e in test1[1:]:
    new_node = ListNode(e)


    cur_pp.next = new_node
    cur_pp = new_node

sln = ReverseKGroupSolution(root, 3)

new_root = sln.solve()

cur_pp = new_root

while cur_pp:
    print(cur_pp.val)
    cur_pp = cur_pp.next