from typing import List, Optional


class Node:
    def __init__(self, next: Optional['Node']):
        self.next: Optional['Node'] = next


class IntersectionSolution:
    def __init__(self, head1: Node, head2: Node):
        self.head1: Node = head1
        self.head2: Node = head2

    def solve(self) -> Optional[Node]:

        curr_node: Optional['Node'] = self.head1

        len_1 = 0

        while curr_node:
            len_1 += 1
            curr_node = curr_node.next

        curr_node = self.head2

        len_2 = 0

        while curr_node:
            len_2 += 1
            curr_node = curr_node.next

        curr_node1 = self.head1
        curr_node2 = self.head2

        if len_1 > len_2:

            for _ in range(len_1 - len_2):
                curr_node1 = curr_node1.next
        elif len_1 < len_2:
            for _ in range(len_2 - len_1):
                curr_node2 = curr_node2.next

        while curr_node1 and curr_node2 and curr_node1 != curr_node2:
            curr_node1 = curr_node1.next
            curr_node2 = curr_node2.next

        return curr_node1
