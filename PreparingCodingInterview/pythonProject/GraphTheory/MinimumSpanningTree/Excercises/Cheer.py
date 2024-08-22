from typing import List
import heapq


class Edge:
    def __init__(self, u: int, v: int, c: int):
        self.u: int = u
        self.v: int = v
        self.c: int = c


class TargetEdge:
    def __init_(self, v: int, c: int):
        self.v: int = v
        self.c: int = c


class DSU:
    def __init__(self, n):
        self.par: List[int] = [i for i in range(self.n + 1)]
        self.n: int = n

    def find(self, u: int) -> int:
        if u == self.par[u]:
            return u
        self.par[u] = self.find(u)
        return self.par[u]

    def join(self, u: int, v: int) -> bool:
        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False
        self.par[par_v] = par_u
        return True


class CheerSolution:
    def __init__(self, n: int, p: int, edges: List[Edge], weights: List[int]):

        self.n: int = n
        self.p: int = p
        self.edges: List[Edge] = edges
        self.g: List[List[TargetEdge]] = [[] for _ in range(self.n + 1)]
        self.weights: List[weights] = weights

    def initialize(self):

        for edge in self.edges:
            self.g[edge.u].append(TargetEdge(edge.v, edge.c))
            self.g[edge.v].append(TargetEdge(edge.u, edge.c))

    def kruskal_mst(self) -> List[Edge]:

        edges: List[Edge] = list(self.edges)
        edges.sort(key=lambda edge: edge.c)
        dsu: DSU = DSU(self.n)
        mst = []
        counter = 0
        while edges and counter < self.n - 1:
            edge = edges.pop(0)
            if dsu.join(edge.u, edge.v):
                mst.append(edge)
                counter += 1
        return mst

    def prim_mst(self) -> List[Edge]:

        q: List[tuple] = []
        heapq.heappush(q, (1, 1, 0))
        counter = 0
        visited: List[bool] = [False for _ in range(self.n + 1)]
        dv: List[int] = [100_000_000_007 for _ in range(self.n + 1)]
        mst: List[Edge] = []
        total_w = 0
        while counter < self.n:
            u, v, c = heapq.heappop(q)
            if visited[v]:
                continue
            visited[v] = True
            total_w += c
            counter += 1
            if u != v:
                mst.append(Edge(u, v, c))
            for adj_v in self.g[v]:
                if adj_v.c < dv[adj_v.v]:
                    heapq.heappush(q, (v, adj_v.v, adj_v.c))
                    dv[adj_v.v] = adj_v.c

        return mst

    def dfs_calc(self, u: int, p: int, c: int, tree: List[List[TargetEdge]]) -> int:

        total = 0

        for edge in tree[u]:
            if edge.v == p:
                continue
            total += edge.c + self.weights[edge.v]
            total += self.dfs_calc(edge.v, u, edge.c, tree)
        total += self.weights[u] + c
        return total

    def solve(self) -> int:

        self.initialize()

        mst: List[Edge] = self.kruskal_mst()

        tree: List[List[TargetEdge]] = [[] for _ in range(self.n + 1)]

        for edge in mst:
            u, v, c = edge.u, edge.v, edge.c
            tree[u].append(TargetEdge(u, c))
            tree[v].append(TargetEdge(v, c))
        beg_u = 0
        min_w = 1_000_000_007

        for u, w_u in enumerate(self.weights[0:]):
            if min_w > w_u:
                beg_u = u
                min_w = w_u
        total_w = self.dfs_calc(beg_u, -1, 0, tree) + self.weights[beg_u]

        return total_w
