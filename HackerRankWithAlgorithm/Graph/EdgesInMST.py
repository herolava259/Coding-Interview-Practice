from typing import List
from enum import Enum


class EdgeType(Enum):
    NONE = 1,
    ANY = 2,
    ATL = 3


class Edge:
    def __init__(self, u: int, v: int, c: int, id: int):
        self.u = u
        self.v = v
        self.c = c
        self.id = id


class Dsu:

    def __init__(self):

        self.par = []

    def reset(self, n: int):

        self.par = [0 for i in range(n + 5)]

    def find(self, u: int):
        if self.par[u] == u:
            return u
        self.par[u] = self.find(self.par[u])

        return self.par[u]

    def join(self, u: int, v: int):
        u, v = self.find(u), self.find(v)

        if u == v:
            return False

        self.par[v] = u

        return True


class TowardEdge:

    def __init__(self, v: int, id: int):
        self.v = v
        self.id = id


class EdgesInMST:
    def __init__(self, g: List[List[TowardEdge]]):
        self.g: List[List[TowardEdge]] = g
        self.n: int = len(self.g)
        self.num: List[int] = [0 for _ in range(self.n)]
        self.low: List[int] = [0 for _ in range(self.n)]
        self.time = 0
        self.res: List[EdgeType] = [EdgeType.NONE for _ in range(self.n)]
        self.dsu: Dsu = Dsu()

    def dfs(self, u: int, idx: int):

        self.time += 1
        self.num[u] = self.low[u] = self.time

        for e in self.g[u]:
            if e.id == idx:
                continue
            if self.num[e.v] == 0:
                self.dfs(e.v, id)
                self.low[u] = min(self.low[u], self.low[e.v])

                if self.low[e.v] == self.num[e.v]:
                    self.res[id] = EdgeType.ANY

            else:
                self.low[u] = min(self.low[u], self.num[e.v])

    def solve(self, pen: List[Edge]):

        if len(pen) == 0:
            return

        for i in range(len(pen)):
            pen[i].u, pen[i].v = self.dsu.find(pen[i].u), self.dsu.find(pen[i].v)
            self.g[pen[i].u] = []
            self.g[pen[i].v] = []
            self.num[pen[i].u] = 0
            self.num[pen[i].v] = 0

        for e in pen:
            if e.u == e.v:
                self.res[e.id] = EdgeType.NONE
            else:
                self.res[e.id] = EdgeType.ATL

                self.g[e.v].append(TowardEdge(e.u, e.id))
                self.g[e.u].append(TowardEdge(e.v, e.id))

        for e in pen:
            if self.num[e.u] == 0:
                self.dfs(e.u, -1)

        for e in pen:
            self.dsu.join(e.u, e.v)

    def run(self, edges: List[Edge], n, m):
        self.dsu.reset(n)
        edges.sort(key=lambda e: e.c)

        pen: List[Edge] = []

        for e in edges:
            if len(pen) != 0 and pen[-1].c == e.c:
                pen.append(e)
            else:
                self.solve(pen)
                pen = [e]

        self.solve(pen)

        return self.res
