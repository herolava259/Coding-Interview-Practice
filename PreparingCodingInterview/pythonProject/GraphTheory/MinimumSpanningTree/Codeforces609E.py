from typing import List


class Edge:
    def __init__(self, u: int, v: int, c: int, eid: int):
        self.u = u
        self.v = v
        self.c = c


class WeightedEdge:
    def __init__(self, v: int, c: int):
        self.v = v
        self.c = c


class Data:
    def __init__(self, par: int, maxc: int):
        self.par = par
        self.maxc = maxc


class Dsu:
    def __init__(self, n: int):

        self.n: int = n
        self.par: List[int] = [i for i in range(self.n + 1)]

    def find(self, u: int) -> int:

        if u == self.par[u]:
            return u

        self.par[u] = self.find(self.par[u])

    def join(self, u: int, v: int) -> bool:

        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False

        self.par[par_v] = par_u
        return True


class MSTOfHasEdgeSolution:
    def __init__(self, n: int, m: int, g: List[List[WeightedEdge]]):
        self.n: int = n
        self.m: int = m
        self.g: List[List[WeightedEdge]] = g
        self.up: List[List[Data]] | None = None
        self.h: List[int] | None = None
        self.in_mst: List[bool] | None = None
        self.edges: List[Edge] | None = None
        self.mst: List[List[int]] | None = None
        self.mst_w: int = 0

    def build(self):
        self.up = [[-1 for _ in range(22)] for _ in range(self.n + 1)]
        self.h = [0 for _ in range(self.n + 1)]
        self.edges = []
        counter = 0
        for u in range(self.n + 1):
            for w_e in self.g[u]:
                self.edges.append(Edge(u, w_e.v, w_e.c, counter))
                counter += 1

        self.in_mst = [False for _ in range(self.m)]

        self.mst_w, mst = self.mst_build()

        self.mst = [[] for _ in range(self.n+1)]

        for e in mst:
            self.mst[e.u].append(e.v)
            self.mst[e.v].append(e.u)

        self.dfs_build(1)
        self.lca_build()

    def dfs_build(self, u: int, p: int = -1):

        self.up[u][0].par = p
        if p != -1:
            self.h[u] = self.h[p] + 1
        for e in self.mst[u]:
            if e.v != p:
                self.up[e.v][0].maxc = e.c
                self.dfs(e.v, u)

    def lca_build(self):

        for i in range(1, 22):
            for u in range(1, self.n + 1):
                self.up[u][i].par = self.up[self.up[u][i - 1].par][i - 1]
                self.up[u][i].par = max(self.up[u][i - 1].maxc, self.up[self.up[u][i - 1].par][i - 1].maxc)

    def mst_build(self) -> (int, List[Edge]):

        dsu = Dsu(self.n)

        total_w: int = 0
        self.edges.sort(key=lambda edge: edge.c)
        mst: List[Edge] = []
        for e in self.edges:
            if not dsu.join(e.u, e.v):
                continue

            total_w += e.c
            mst.append(e)
            self.in_mst[e.id] = True

        return total_w, mst

    def lca_query_max(self, u, v) -> int:

        res = -100_000_007

        if self.h[u] < self.h[v]:
            u, v = v, u

        diff_h = self.h[u] - self.h[v]

        for i in range(22):
            if (diff_h >> i) & 1 == 1:
                res = max(res, self.up[u][i].maxc)
                u = self.up[u][i].par

        if u == v:
            return res

        for i in range(21, -1, -1):
            if self.up[u][i].par == self.up[v][i].par:
                continue
            res = max(res, self.up[u][i].maxc, self.up[v][i].maxc)
            u, v = self.up[u][i].par, self.up[v][i].par

        res = max(res, self.up[u][0].maxc, self.up[v][0].maxc)

        return res

    def mst_query(self, eid: int) -> int:
        if self.in_mst[eid]:
            return self.mst_w

        return self.mst - self.lca_query_max(self.edges[eid].u, self.edges[eid].v) + self.edges[eid].c

    def solve(self) -> List[int]:

        res = [0 for _ in range(self.m)]

        for eid in range(self.m):
            res[eid] = self.mst_query(eid)

        return res