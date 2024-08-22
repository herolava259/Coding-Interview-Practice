from typing import List, Deque, Optional
from collections import deque


class ListNode:
    def __init__(self, idx: int, val: int, nxt_node: Optional['ListNode'] = None):
        self.idx: int = idx
        self.val: int = val
        self.nxt_node = nxt_node


class GreedySubsequenceSolution:
    def __init__(self, n: int, k: int, c: List[int]):
        self.n: int = n
        self.k: int = k
        self.c: List[int] = c

    def solve(self) -> List[int]:

        gt_idx = [-1 for _ in range(self.n)]

        res: List[int] = [0 for _ in range(self.n)]

        nodes = [ListNode(idx, val) for idx, val in enumerate(self.c)]

        s: deque = deque()
        s.append((self.n - 1, self.c[self.n - 1]))
        for idx in range(self.n - 2, -1, -1):
            while s and s[-1][1] <= self.c[idx]:
                s.pop()

            if s:
                gt_idx[idx] = s[-1][0]
                nodes[idx].nxt_node = nodes[gt_idx[idx]]

        for idx in range(self.n):

            counter = 1
            cur_p = nodes[idx]
            cur_win_idx = max(0, idx - self.k)

            while cur_win_idx <= idx:
                while cur_p.nxt_node and cur_p.nxt_node.idx <= cur_win_idx + self.k:
                    cur_p = cur_p.nxt_node
                    counter += 1
                res[cur_win_idx] = max(res[cur_win_idx], counter)
                cur_win_idx += 1

        return res


n1, k1 = 6, 4
c1 = [1, 5, 2, 5, 3, 6]

sln = GreedySubsequenceSolution(n1, k1, c1)

print(sln.solve())
