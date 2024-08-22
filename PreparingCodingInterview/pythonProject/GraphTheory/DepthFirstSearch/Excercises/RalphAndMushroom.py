from typing import List, DefaultDict, Dict
from collections import deque, defaultdict


class TargetEdge:
    def __init__(self, v: int, c: int):
        self.v: int = v
        self.c: int = c


class StrongConnectedComponent:
    def __init__(self, root: int, nodes: List[int], edges: DefaultDict[List[TargetEdge]]):
        self.nodes: List[int] = nodes
        self.edges: DefaultDict[List[TargetEdge]] = edges
        self.root: int = root

    def calc_maximum_mushroom(self) -> int:
        res: int = 0

        for k in self.edges.keys():
            edges: List[TargetEdge] = self.edges[k]

            for e in edges:
                c = e.c
                i = 1
                while c > 0:
                    res += c
                    c -= i
                    i += 1

        return res


class RalphAndMushroomSolution:

    def __init__(self, m: int, n: int, g: List[List[TargetEdge]], s: int):
        self.m: int = m
        self.n: int = n
        self.g: List[List[TargetEdge]] = g
        self.s: int = s

        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]
        self.tail: List[int] = [0 for _ in range(self.n + 1)]

        self.time: int = 0
        self.frees: List[bool] = [True for _ in range(self.n + 1)]

        self.components: Dict[int, StrongConnectedComponent] = dict()
        self.scc_tree: DefaultDict[int, List[TargetEdge]] = defaultdict(list)
        self.root: List[int] = [0 for _ in range(self.n + 1)]

        self.st: deque = deque()
        self.cross_edges: List[tuple] = []

    def dfs_solve(self, u: int):
        self.time += 1

        self.num[u] = self.low[u] = self.time
        for e_v in self.g[u]:
            v: int = e_v.v

            if not self.frees[v]:
                if not (self.num[v] <= self.num[u] <= self.tail[v]):
                    self.cross_edges.append((u, v, e_v.c))
                continue
            if self.num[v] == 0:
                self.st.append((u, v, e_v.c))
                self.dfs_solve(v)
                self.low[u] = min(self.low[v], self.low[u])
            else:
                self.st.append((u, v, e_v.c))
                self.low[u] = min(self.num[v], self.low[u])

        self.tail[u] = self.time
        if self.low[u] == self.num[u]:
            self.crack_graph(u)

    def crack_graph(self, u: int):

        head = self.num[u]
        tail = self.tail[u]

        cur_u, cur_v, cur_c = self.st.pop()
        nodes: set = set()
        scc: DefaultDict[List[TargetEdge]] = defaultdict(list)
        while head <= self.num[cur_u] <= tail:
            nodes.add(cur_u)
            nodes.add(cur_v)

            self.frees[cur_u] = False
            self.frees[cur_v] = False

            self.root[cur_u] = self.root[cur_v] = u

            scc[cur_u].append(TargetEdge(cur_v, cur_c))
            cur_u, cur_v, cur_c = self.st.pop()

        self.components[u] = StrongConnectedComponent(u, list(nodes), scc)

    def solve(self) -> int:

        self.dfs_solve(self.s)

        for e in self.cross_edges:
            u, v, c = e

            self.scc_tree[self.root[u]].append(TargetEdge(self.root[v], c))

        incomes: DefaultDict[int, int] = defaultdict(int)

        for r in self.components.keys():
            incomes[r] = self.components[r].calc_maximum_mushroom()

        return self.dfs_income(self.root[self.s], incomes=incomes)

    def dfs_income(self, u: int, incomes: DefaultDict[int, int]) -> int:

        res = -1
        income_u = incomes[u]

        for e in self.scc_tree[u]:
            res_v = self.dfs_income(e.v, incomes)

            if res_v + income_u + e.c > res:
                res = res_v + income_u + e.c

        return res

