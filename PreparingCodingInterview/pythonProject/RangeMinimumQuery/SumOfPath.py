from typing import List
from LowestCommonAncestor import SparseTableLCASolution
from RangeMinimumQuery import SparseTableRMQSolution

class BuildingEulerPathInTree:
    def __init__(self, n: int, m: int, g: List[List[int]], root: int | None = None):
        self.m = m
        self.n = n
        self.g = g
        self.time = 0
        self.starts: List[int] = [0 for _ in range(self.n + 1)]
        self.ends: List[int] = [0 for _ in range(self.n + 1)]
        self.tour: List[int] = []
        self.h: List[int] = [0 for _ in range(self.n + 1)]
        self.root = root if root is not None else 1
        self.arg_time = [0 for _ in range(self.n + 1)]

    def add(self, u: int):
        self.time += 1
        self.tour.append(self.starts[u])
        self.ends[u] = self.time

    def dfs(self, u: int, p: int):
        self.h[u] = self.h[p] + 1
        self.add(u)
        self.starts[u] = self.time
        self.arg_time[self.time] = u
        for v in self.g[u]:
            if v != p:
                self.dfs(v, u)

        if p != self.root and p != -1:
            self.add(p)

    def solve(self) -> List[int]:

        self.time = 0
        self.tour = []

        self.dfs(self.root, -1)

        return self.tour


class SumOfPathByLCASolution:
    def __init__(self, n: int, g: List[List[int]], root: int, values: List[int]):
        self.n = n
        self.g = g
        self.values = values
        self.root = root
        self.sum_to_root = [0 for _ in range(self.n + 1)]
        self.sum_to_root[self.root] = self.values[root]
        self.lca_sln = SparseTableLCASolution(g, root)
        self.parents = [-1 for _ in range(self.n + 1)]

    def initialize(self):
        self.lca_sln.initialize()
        self.dfs_build()

    def dfs_build(self, u: int, p: int):
        self.parents[u] = p
        if p != -1:
            self.sum_to_root[u] = self.sum_to_root[p] + self.values[u]

        for v in self.g[u]:
            if v != p:
                self.dfs_build(v, u)

    def query_sum(self, u: int, v: int):

        lca = self.lca_sln.lca_query(u, v)

        lca_to_root = 0

        if lca != self.root:
            lca_to_root = self.sum_to_root[self.parents[lca]]

        return self.sum_to_root[u] + self.sum_to_root[v] - lca_to_root << 1

class SumOfPathByRMQSolution:
    def __init__(self, n: int,m:int, g: List[List[int]], root: int, values: List[int]):
        self.n = n
        self.m = m
        self.g = g
        self.root = root
        self.values = values
        self.flatten_tree = BuildingEulerPathInTree(n, m, g, root)
        self.rmq_sln: SparseTableRMQSolution | None = None
        self.tour: List[int] | None = None
        self.st: List[int] | None = None
        self.en: List[int] | None = None
        self.parents: List[int] = [0 for _ in range(self.n+1)]
        self.sums: List[int] = [-1 for _ in range(self.n+1)]

    def dfs_build(self, u: int, p: int = -1):
        self.parents[u] = p
        if p != -1:
            self.sums[u] = self.sums[p] + self.values[u]

        for v in self.g[u]:
            if v != p:
                self.dfs_build(v, u)

    def initialize(self):
        self.dfs_build(self.root)
        self.tour = self.flatten_tree.solve()
        self.st = self.flatten_tree.starts
        self.en = self.flatten_tree.ends
        self.rmq_sln = SparseTableRMQSolution(self.tour)

    def query_sum(self, u: int, v: int):

        if self.st[u] > self.st[v]:
            u, v = v, u

        beg_idx = min(self.st[u], self.st[v])
        end_idx = max(self.en[u], self.en[v])

        lca = self.find_lca(beg_idx, end_idx)

        sum_p_lca = 0

        if lca != self.root:
            sum_p_lca = self.sums[self.parents[lca]]

        return self.sums[u] + self.sums[v] - 2 * sum_p_lca

    def find_lca(self, first: int, last: int) -> int:
        _, lca_arg_time = self.rmq_sln.query(first-1, last-1)
        lca = self.flatten_tree.arg_time[lca_arg_time-1]
        return lca






