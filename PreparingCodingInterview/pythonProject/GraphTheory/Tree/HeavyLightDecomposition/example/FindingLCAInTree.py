from pythonProject.GraphTheory.Tree.HeavyLightDecomposition.base.BuildingHLD import HLDBuilder
from pythonProject.GraphTheory.Tree.HeavyLightDecomposition.base.HLDStructure import GeneralHLDTree as HLD
from typing import List

class FindingLCASolution:
    def __init__(self, tree: List[List[int]], root: int, u: int, v: int):
        self.tree: List[List[int]] = tree
        self.root: int = root
        self.u: int = u
        self.v: int = v

    def solve(self) -> int:
        hld: HLD = (HLDBuilder().add_root(self.root)
                                    .add_tree(self.tree)
                                    .init_spec()
                                    .build())
        head_chain_of = lambda nid: hld.par[hld.chain_head[hld.chain_id[nid]]]

        u, v = self.u, self.v
        while hld.chain_id[u] != hld.chain_id[v]:
            if hld.chain_id[u] > hld.chain_id[v]:
                u = hld.par[head_chain_of(u)]
            else:
                v = hld.par[head_chain_of(v)]

        if hld.depth[u] < hld.depth[v]:
            return u

        return v

class QueryLCAResolver:
    def __init__(self, tree: List[List[int]], root: int):
        self.tree: List[List[int]] = tree
        self.root: int = root
        self.hld: HLD = (HLDBuilder().add_root(self.root)
                    .add_tree(self.tree)
                    .init_spec()
                    .init_spec()
                    .build())

    def query(self, u: int, v: int) -> int:

        head_chain_of = lambda nid: self.hld.par[self.hld.chain_head[self.hld.chain_id[nid]]]

        while self.hld.chain_id[u] != self.hld.chain_id[v]:
            if self.hld.chain_id[u] > self.hld.chain_id[v]:
                u = self.hld.par[head_chain_of(u)]
            else:
                v = self.hld.par[head_chain_of(v)]

        if self.hld.depth[u] < self.hld.depth[v]:
            return u

        return v
