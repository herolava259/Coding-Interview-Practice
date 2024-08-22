from typing import List, Optional


class Node:
    def __init__(self, sig: str = '', nxt: Optional['Node'] = None):
        self.next: Optional['Node'] = nxt
        self.sig: str = sig


class LoopDetectionSolution:

    def __init__(self, head: Node):
        self.head: Node = head

    def solve(self) -> Node | None:
        vir_tail = Node()

        curr_node = vir_tail

        while curr_node.next or curr_node.next == vir_tail:
            nxt_node = curr_node.next

            curr_node.next = vir_tail
            curr_node = nxt_node

        return curr_node.next

    def solve_without_destruct(self) -> Node | None:

        slow_node = self.head
        fast_node = self.head
        if fast_node.next is None or fast_node.next.next is None:
            return None
        loop_k = 0
        while fast_node.next and fast_node.next.next and slow_node != fast_node.next.next \
                and slow_node != fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            loop_k += 1

        if fast_node.next is None or fast_node.next.next is None:
            return None

        curr_node = self.head
        loop_k += 1
        while loop_k:
            fast_node = slow_node.next
            while curr_node != fast_node and fast_node != slow_node:
                fast_node = fast_node.next
            if curr_node == fast_node:
                return curr_node
            curr_node = curr_node.next
            loop_k -= 1

        return None

node_a, node_b, node_c, node_d, node_e = Node('a'), Node('b'), Node('c'), Node('d'), Node('e')

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
node_e.next = node_c

sln = LoopDetectionSolution(node_a)


ret_node = sln.solve_without_destruct()
print("sig of ret_node: ", ret_node.sig)
print('end')

