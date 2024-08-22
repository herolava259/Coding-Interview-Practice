from typing import List
from typing import Optional


class Node:
    def __init__(self, val: int, eid: int, left_node: Optional = None, right_node: Optional = None):
        self.val: int = val
        self.eid: eid = eid
        self.left_node = left_node
        self.right_node = right_node
        self.par = None


class BuildingCatersianTreeSolution:
    def __init__(self, arr: List[int], n: int | None = None):
        self.arr = arr
        self.n = n if n is not None else len(arr)
        self.tree = [Node(val, eid) for eid, val in enumerate(arr)]
        self.root: Node | None = None

    def build(self) -> Node | None:
        if self.root is not None:
            return self.root
        s: List[tuple] = [(0, self.arr[0])]

        for eid, e in enumerate(self.arr):
            child_id = None
            while not s and s[-1][1] > e:
                child_id, _ = s.pop()
            if child_id is not None:
                self.tree[eid].left_node = self.tree[child_id]
                self.tree[child_id].par = self.tree[eid]
            if len(s) > 0:
                self.tree[s[-1][0]].right_node = self.tree[eid]
                self.tree[eid].par = self.tree[s[-1][0]]
            s.append((eid, e))

        self.root = self.tree[s[0][0]] if len(s) > 0 else None

        return self.root
