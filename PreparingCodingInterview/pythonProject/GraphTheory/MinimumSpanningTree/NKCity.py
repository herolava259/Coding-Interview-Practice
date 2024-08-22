from typing import List
from DisjoinSetUnion import Edge, DSU


class NKCitySolution:
    def __init__(self, n: int, m: int, edges: List[Edge]):
        self.n = n
        self.m = m
        self.edges = edges

    def solve(self) -> int:

        max_w = 100_000_007
        dsu = DSU(self.n)

        self.edges.sort(key= lambda edge: edge.c)

        for e in self.edges:

            if dsu.join(e.u, e.v) and e.c > max_w:
                max_w = e.c

        return max_w
