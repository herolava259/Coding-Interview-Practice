from typing import Tuple

from FindingLCAInTree import QueryLCAResolver as LCAResolver
from pythonProject.GraphTheory.Tree.HeavyLightDecomposition.base.HLDStructure import GeneralHLDTree as HLD
from typing import List

class SegmentTree:
    def __init__(self, max_size: int = 100000):

        self.max_size: int = max_size

        self.st: List[int] = [0] * (4* max_size)

        self.size: int = 0

    def initialize(self, arr: List[int]):

        def build(idx: int, l: int, r: int):

            if l == r:
                self.st[idx] = arr[l]
                return

            mid = (l + r ) >> 1
            left_idx = idx << 1
            right_idx = left_idx + 1
            build(left_idx, l, mid)
            build(right_idx, mid + 1, r)

            self.st[idx] = self.st[left_idx] ^ self.st[right_idx]

        build(1, 0, len(arr)-1)
        self.size = len(arr)


    def update(self, idx: int, l: int, r: int, pos: int, val: int):

        if l > pos or r < pos:
            return

        if l == r and l == pos:
            self.st[idx] = val
            return

        mid: int = (l + r) >> 1

        left_idx = idx << 1
        right_idx = left_idx + 1

        self.update(left_idx, l, mid, pos, val)
        self.update(right_idx, mid+1, r, pos, val)

        self.st[idx] = self.st[left_idx] ^ self.st[right_idx]


    def calc(self, idx: int, tl: int, tr: int, l: int, r: int) -> int:

        if tl > r or tr < l:
            return 0

        if l <= tl and tr <= r:
            return self.st[idx]

        tmid: int = (tl + tr) >> 1

        return self.calc(idx << 1, tl, tmid, l, r) ^ self.calc((idx << 1) + 1, tmid+1, tr, l, r)


class XorSumInTreeResolver:
    def __init__(self, root: int, tree: List[List[int]], val: List[int]):

        self.root: int = root
        self.tree: List[List[int]] = tree
        self.n = len(self.tree)
        self.st: SegmentTree = SegmentTree()
        self.lca_resolver = LCAResolver(tree, root)
        self.hld: HLD = self.lca_resolver.hld

        arrange_val = [0] + [val[self.hld.inverse_pos[pos]] for pos in range(1, self.n+1)]
        self.st.initialize(arrange_val)



    def update(self, x: int, val: int):
        self.st.update(1, 1, self.n, self.hld.pos[x], val)


    def query(self, u: int, v: int) -> int:

        lca: int = self.lca_resolver.query(u, v)

        chain_head_of = lambda nid: self.hld.chain_head[self.hld.chain_id[nid]]


        def xor_in_heavy_path(uid: id, aid: int) -> Tuple[int, int]:
            res = 0

            while self.hld.chain_id[uid] != self.hld.chain_id[aid]:
                chain_head_u = chain_head_of(uid)
                res ^= self.st.calc(1, 1, self.n, self.hld.pos[chain_head_u], self.hld.pos[u])
                uid = self.hld.par[chain_head_u]
            return uid, res

        u, res_u = xor_in_heavy_path(u, lca)
        v, res_v = xor_in_heavy_path(v, lca)

        ans = res_u ^ res_v


        if self.hld.depth[u] < self.hld.depth[v]:
            u, v = v, u

        ans ^= self.st.calc(1, 1, self.n, self.hld.pos[u], self.hld.pos[v])

        return ans
    










