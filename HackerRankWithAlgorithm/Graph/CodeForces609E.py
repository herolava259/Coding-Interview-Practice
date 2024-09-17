from typing import List


class Edge:
    def __init__(self, u: int, v: int, c:int, id: int):
        self.u = u
        self.v = v
        self.c = c
        self.id = id

class Data:
    def __init__(self, par: int, maxc: int):
        self.par= par
        self.maxc = maxc

class Dsu:
    def __init__(self):
        self.par: List[int] = []

    def reset(self, n: int):
        self.par = [i for i in range(n+5)]

    def find(self, u:int):

        if self.par[u] == u:
            return u

        self.par[u] = self.find(self.par[u])

        return self.par[u]

    def join(self, u: int, v: int) -> bool:
        u, v = self.find(u), self.find(v)

        if u == v:
            return False
        self.par[v] = u
        return True

class TowardEdge:

    def __init__(self, v: int, c: int):

        self.v = v
        self.c = c

INF = 1000000007

class FindMSTOfEdgeSolution:

    def __init__(self, n: int, m: int, edges: List[Edge]):
        self.n = n
        self.m = m
        self.edges = edges
        self.up: List[List[Data]] = []
        self.g: List[List[TowardEdge]] = [[] for _ in range(n)]
        self.h:List[int] = [0 for _ in range(n+1)]
        self.res: List[int] = [0 for _ in range(m)]
        self.dsu = Dsu()
        self.mstWeight = 0

    def dfs(self, u: int, p: int):
        self.up[u][0] = p;

        for e in self.g[u]:

            if e.v == p:
                continue
            self.h[e.v] = self.h[e.u] + 1
            self.up[e.v][0].maxc = e.c
            self.dfs(e.v, u)
    def bit(self, depth, i):
        return 1 & (depth >> i)
    def lca(self, u, v) -> int:
        ret = -INF
        if self.h[u] < self.h[v]:
            u, v = v, u
        depth = self.h[u] - self.h[v]

        for i in range(21):
            if self.bit(depth, i):
                ret = max(ret, self.up[u][i].maxc)
                u = self.up[u][i].par

        if u == v:
            return ret

        for i in range(20, -1, -1):
            if self.up[u][i].par != self.up[v][i].par:
                ret = max(ret, self.up[u][i].maxc, self.up[v][i].maxc)
                u, v = self.up[u][i].par, self.up[v][i].par

            ret = max(ret, self.up[u][0].maxc, self.up[v][0].maxc)
            return ret

    def buildMST(self):

        self.dsu.reset()

        self.edges.sort(key= lambda e: e.c)

        for e in self.edges:
            if not self.dsu.join(e.u, e.v):
                continue

            self.g[e.u].append(TowardEdge(e.v, e.c))
            self.g[e.v].append(TowardEdge(e.u, e.c))

            self.res[e.id] = -1
            self.mstWeight += e.c

    def buildLCA(self):
        self.dfs(1,1)

        for i in range(1, 20, 1):
            for u in range(1, self.n, 1):
                self.up[u][i].par = self.up[self.up[u][i-1].par][i-1].par
                self.up[u][i].maxc = max(self.up[u][i-1].maxc, self.up[self.up[u][i-1].par][i-1].maxc)

    def solve(self) -> List[int]:

        self.buildMST()
        self.buildLCA()

        for e in self.edges:
            if self.res[id] == -1:
                self.res[id] = self.mstWeight
            else:
                self.res[e.id] = self.mstWeight - self.lca(e.u, e.v) + e.c

        return self.res

