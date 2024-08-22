from typing import DefaultDict, Optional, List
from collections import defaultdict


class DSUNode:
    def __init__(self, val: int):
        self.is_par = True
        self.num_consecutive = 1
        self.val = val
        self.par: DSUNode = None

    def find_par(self) -> Optional['DSUNode']:
        if self.is_par or self.par is None:
            return self
        self.par = self.par.find_par()
        return self.par

    def join(self, v: Optional['DSUNode']) -> bool:

        par_self = self.find_par()
        par_v = v.find_par()

        if par_self.val == par_v.val:
            return False

        par_v.is_par = False
        par_v.par = par_self

        par_self.num_consecutive += par_v.num_consecutive
        return True


class LCSSolution:

    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> int:
        dsu_tb: DefaultDict[int, DSUNode | None] = defaultdict(lambda: None)

        max_cons = 0

        for e in self.nums:

            cur_node = dsu_tb[e]

            if cur_node is None:
                dsu_tb[e] = DSUNode(e)
                cur_node = dsu_tb[e]

            prev_node = dsu_tb[e - 1]
            nxt_node = dsu_tb[e + 1]

            if prev_node is not None:
                cur_node.join(prev_node)
            if nxt_node is not None:
                nxt_node.join(cur_node)

            par_node = cur_node.find_par()

            max_cons = max(max_cons, par_node.num_consecutive)

        return max_cons

nums1 = [100,4,200,1,3,2]

sln = LCSSolution(nums1)

print(sln.solve())


