from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class NRPByFlattenTreeSolution:
    def connect(self, root: 'Node') -> 'Node':
        max_level = self.max_height(root)
        arr: List[Optional['Node']] = [None for _ in range(2 << max_level + 1)]
        self.flatten(arr, root, 1)

        level = 1

        for level in range(1, max_level + 1):
            first = (2 << (level - 1))
            last = (2 << level)

            idx = first
            while idx < last and arr[idx] is None:
                idx += 1
            next_idx = idx + 1

            while idx < last:
                while next_idx < last and arr[next_idx] is None:
                    next_idx += 1
                if next_idx < last:
                    arr[idx].next = arr[next_idx]
                idx = next_idx
                next_idx += 1

        return root

    def max_height(self, root: Optional['Node']) -> int:

        if root is None:
            return 0
        return 1 + max(self.max_height(root.left), self.max_height(root.right))

    def flatten(self, arr: List[Optional['Node']], root_node: Optional['Node'], idx: int):
        if root_node is None:
            return
        arr[idx] = root_node
        self.flatten(arr, root_node.left, 2 * idx)
        self.flatten(arr, root_node.right, 2 * idx + 1)


class NormalNRPSolution:
    def __init__(self, root: Node):
        self.root: Node = root

    def solve(self, root_node: Node | None, h: int, right_most_arr: List[Node]):
        if root_node is None:
            return
        root_node.next = right_most_arr[h]
        right_most_arr[h] = root_node

        self.solve(root_node.right, h + 1, right_most_arr)
        self.solve(root_node.left, h + 1, right_most_arr)

    def connect(self) -> Node:
        right_most_arr: List[Node | None] = [None for _ in range(10000)]

        self.solve(self.root, 0, right_most_arr)

        return self.root
