from typing import List
import heapq


class Edge:
    def __init__(self, eid: int, u: int, v: int, weight: int):
        self.eid: int = eid
        self.u: int = u
        self.v: int = v
        self.weight: int = weight


max_value = 2 * 10 ** 9 + 7


class PrimMSTSolution:
    def __init__(self, n: int, edges: List[Edge]):
        self.n: int = n
        self.edges: List[Edge] = edges

    def solve(self) -> (int, List[Edge]):

        g = List[List[(int, int)]] = [[] for _ in range(self.n)]

        for edge in self.edges:
            g[edge.u].append((edge.v, edge.weight))
            g[edge.v].append((edge.u, edge.weight))
        total_w: int = 0
        prior_q: List[tuple] = [(0, 0, 0)]

        mst: List[Edge] = []
        visited: List[bool] = [False for _ in range(self.n)]
        min_dv: List[int] = [max_value for _ in range(self.n)]
        counter: int = 0
        while prior_q:
            u, v, c = heapq.heappop(prior_q)

            if visited[v]:
                continue
            total_w += c
            visited[v] = True
            if u != v:
                mst.append(Edge(counter, u, v, c))
                counter += 1

            # update min dv from v( v is not visited to s)

            for v, c_v in g[u]:
                if visited[v]:
                    continue
                if min_dv[v] > c_v:
                    min_dv[v] = c_v
                    heapq.heappush(prior_q, (u, v, c_v))

        return total_w, mst


class Dsu:
    def __init__(self, n: int):
        self.n = n
        self.par: List[int] = [i for i in range(n)]

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


class KruskalMSTSolution:
    def __init__(self, n: int, edges: List[Edge]):
        self.n: int = n
        self.edges: List[Edge] = edges

    def solve(self) -> (int, List[Edge]):

        total_w: int = 0
        mst: List[Edge] = []

        counter = 0
        edges = [edge for edge in self.edges]
        edges.sort(key=lambda edge: edge.weight)
        dsu = Dsu(self.n)
        while counter < self.n:
            edge = self.edges.pop(0)
            if dsu.join(edge.u, edge.v):
                total_w += edge.weight
                mst.append(edge)
                counter += 1
        return total_w, mst


class P186SumFSolution:
    def __init__(self, n: int, node_weights: List[int], g: List[List[int]]):

        self.n = n
        self.node_weights: List[int] = node_weights
        self.g: List[List[int]] = g
        self.edges: List[Edge] = []

    def build(self):

        counter = 0
        marks: List[List[int]] = [[False for _ in range(self.n)] for _ in range(self.n)]
        for u in range(self.n):
            for v in self.g[u]:
                if marks[u][v]:
                    continue
                self.edges.append(Edge(counter, u, v, self.node_weights[u] ^ self.node_weights[v]))
                marks[u][v] = True
                marks[v][u] = True
                counter += 1

    def solve_by_prim_sln(self) -> int:

        prim_sln = PrimMSTSolution(self.n, self.edges)

        total_w, _ = prim_sln.solve()

        return total_w

    def solve_by_kruskal_sln(self) -> int:
        kruskal_sln = KruskalMSTSolution(self.n, self.edges)

        total_w, _ = kruskal_sln.solve()

        return total_w
