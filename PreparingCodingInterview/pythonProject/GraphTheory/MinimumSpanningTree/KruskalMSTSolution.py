from typing import List
from DisjoinSetUnion import Edge, DSU


class KruskalMSTSolution:
    def __init__(self, edges: List[Edge], n: int):

        self.n: int = n
        self.edges: List[Edge] = edges
        self.m = len(edges)
        self.dsu = DSU(n)

    def solve(self) -> (int, List[Edge]):

        self.edges.sort(key=lambda edge: edge.c)

        total_w: int = 0
        mst: List[Edge] = []

        for e in self.edges:
            if self.dsu.join(e.u, e.v):
                total_w += e.c
                mst.append(e)

        return total_w, mst

