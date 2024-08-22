from typing import List

from enum import Enum


class Type(Enum):
    NONE = 1,
    ANY = 2,
    ATL = 3


class Edge:
    def __init__(self, u: int, v: int, c: int, eid: int):
        self.u: int = u
        self.v: int = v
        self.c: int = c
        self.eid: int = eid


class Dsu:
    def __init__(self, n: int):
        self.n = n
        self.par = [i for i in range(self.n + 1)]

    def find(self, u: int) -> int:
        if u == self.par[u]:
            return u

        self.par[u] = self.find(self.par[u])

        return self.par[u]

    def join(self, u: int, v: int):
        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False

        self.par[par_v] = par_u


class TargetEdge:
    def __init__(self, v: int, eid: int):
        self.v, self.eid = v, eid


class EdgesInTreeSolution:
    def __init__(self, n: int, m: int, g: List[List[TargetEdge]]):

        self.n: int = n
        self.m: int = m
        self.g: List[List[TargetEdge]] = g
        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]
        self.time: int = 0
        self.edge_types: List[Type] = [Type.NONE for _ in range(self.n + 1)]
        self.edges: List[Edge] = []
        self.dsu: Dsu = Dsu(self.n)

    def reset(self):
        self.low = [0 for _ in range(self.n + 1)]
        self.num = [0 for _ in range(self.n + 1)]
        self.time = 0

    def dfs(self, u: int, idx: int):

        self.time += 1
        self.num[u] = self.low[u] = self.time

        for e_v in self.g[u]:
            if e_v.eid == idx:
                continue

            if self.num[e_v.v] == 0:
                self.dfs(e_v.v, e_v.eid)
                self.low[u] = min(self.low[u], self.low[e_v.v])
                if self.low[e_v.v] == self.num[e_v.v]:
                    self.edge_types[e_v.eid] = Type.ANY

            else:
                self.low[u] = min(self.low[u], self.low[e_v.v])

    def judgment_level(self, pen: List[Edge]):

        if len(pen) == 0:
            return

        # init
        for edge in pen:
            edge.u = self.dsu.find(edge.u)
            edge.v = self.dsu.find(edge.v)

            self.g[edge.u].clear()
            self.g[edge.v].clear()

            self.num[edge.u] = 0
            self.num[edge.v] = 0

        # setup and judment None and ATL
        for edge in pen:
            if edge.u == edge.v:
                self.edges[edge.eid] = Type.NONE

            else:
                self.edges[edge.eid] = Type.ATL
                self.g[edge.v].append(TargetEdge(edge.u, edge.eid))
                self.g[edge.u].append(TargetEdge(edge.v, edge.eid))

        # find and edge

        for e in pen:
            if self.num[e.u] == 0:
                self.dfs(e.u, -1)

        for e in pen:
            self.dsu.join(e.u, e.v)

    def solve(self) -> List[Type]:

        self.reset()

        pen: List[Edge] = []

        self.edges.sort(key=lambda e: e.c)
        for e in self.edges:
            if len(pen) != 0 and pen[-1].c == e.c:
                pen.append(e)
            else:
                self.judgment_level(pen)
                pen = [e]

        self.judgment_level(pen)

        return self.edges
