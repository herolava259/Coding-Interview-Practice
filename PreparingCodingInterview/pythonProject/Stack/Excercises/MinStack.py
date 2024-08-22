from typing import Optional


class StackNode:
    def __init__(self, value: int, min_value: int, next_node: Optional['StackNode'] = None):
        self.value: int = value
        self.min_value: int = min_value
        self.next_node: Optional['StackNode'] = next_node


class MinStack:
    def __init__(self):
        self.top_node: StackNode | None = None

    def min_value(self) -> int | None:
        if self.top_node is None:
            return None
        return self.top_node.min_value

    def push(self, val: int):

        new_node: StackNode = StackNode(val, val, self.top_node)

        if self.top_node and new_node.min_value > self.top_node.min_value:
            new_node.min_value = self.top_node.min_value

        self.top_node = new_node

    def pop(self) -> int | None:

        curr_node = self.top_node
        if curr_node is None:
            return None
        self.top_node = curr_node.next_node

        return curr_node.value

    def peek(self, idx: int = 0) -> int | None:

        curr_node = self.top_node

        while idx > 0 and curr_node is not None:
            curr_node = curr_node.next_node
            idx -= 1
        return curr_node.value if curr_node else None

    def is_empty(self) -> bool:
        return True if self.top_node is None else False
