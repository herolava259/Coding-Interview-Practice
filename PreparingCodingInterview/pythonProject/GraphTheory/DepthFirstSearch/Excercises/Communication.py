from collections import deque, defaultdict
from typing import List, Deque, Set, DefaultDict


class DSU:
    def __init__(self, n: int):
        self.par: List[int] = [i for i in range(n + 1)]

    def find(self, u: int) -> int:
        if self.par[u] == u:
            return u
        self.par[u] = self.find(self.par[u])

        return self.par[u]

    def join(self, u: int, v: int) -> bool:

        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False

        self.par[par_v] = par_u
        return True


class CommunicationSolution:

    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n

        self.g: List[List[int]] = g

        self.low: List[int] = [0 for _ in range(n + 1)]
        self.num: List[int] = [0 for _ in range(n + 1)]
        self.free: List[bool] = [True for _ in range(n + 1)]

        self.time = 0
        self.st: Deque[int] = deque()

        self.root: List[int] = [0 for _ in range(self.n + 1)]
        self.dsu: DSU = DSU(n)

    def dfs_solve(self, u: int, p: int):
        self.time += 1
        self.low[u] = self.num[u] = self.time
        self.st.append(u)
        for v in self.g[u]:
            if (not self.free[v]) or v == p:
                continue

            if self.num[v] == 0:
                self.dfs_solve(v, u)

                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.low[u] = min(self.low[u], self.num[v])

        if self.low[u] == self.num[u]:
            self.crack_graph(u)

    def crack_graph(self, u: int):

        cur_node = self.st.pop()
        self.free[cur_node] = False

        self.root[cur_node] = u
        while cur_node != u:
            cur_node = self.st.pop()
            self.free[cur_node] = False
            self.root[cur_node] = u

    def solve_by_dsu(self) -> int:
        for u in range(1, self.n + 1):
            for v in self.g[u]:
                self.dsu.join(u, v)
        root_set: Set[int] = set()

        for u in range(1, self.n + 1):
            root_set.add(self.dsu.find(u))

        return len(root_set)

    def solve_by_scc(self) -> int:

        self.time = 0
        self.st.clear()
        for u in range(1, self.n + 1):
            if self.num[u] == 0:
                self.dfs_solve(u, 0)

        root_scc: Set[int] = set()
        has_in: DefaultDict[int, bool] = defaultdict(bool)
        for u in range(1, self.n + 1):
            root_u = self.root[u]
            root_scc.add(root_u)
            for v in self.g[u]:
                root_v = self.root[v]
                if root_u != root_v:
                    has_in[root_v] = True

        num_comm = 0
        for u in root_scc:
            if not has_in[u]:
                num_comm += 1

        return num_comm
