from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root: Optional[TreeNode] = root
        self.cur_p: int = -1
        arr = []
        self.flatten(self.root, arr)
        self.arr: List[int] = arr
        self.n: int = len(arr)

    def flatten(self, cur_node: TreeNode | None, arr: List[int]):
        if not cur_node:
            return
        self.flatten(cur_node.left, arr)
        arr.append(cur_node.val)
        self.flatten(cur_node.right, arr)

    def hasNext(self) -> bool:
        return self.cur_p + 1 < self.n

    def next(self) -> int:
        if self.hasNext():
            self.cur_p += 1
            return self.arr[self.cur_p]
        return -1
