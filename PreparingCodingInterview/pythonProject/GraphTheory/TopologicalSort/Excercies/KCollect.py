from typing import List, Type
from collections import deque
from collections import defaultdict


class KCollectAdapter:
    def __init__(self, m: int, n: int, raw_inp: str):

        self.m = m
        self.n = n
        self.raw_inp: str = raw_inp
        self.matrix: List[str] | None = None
        self.g: List[dict] | None = None

    def build(self) -> list[Type[dict]]:

        self.matrix = self.raw_inp.split('\n')
        self.g = [dict for _ in range(self.m * self.n)]
        for i in range(self.m):
            for j in range(self.n):
                idx = self.n * i + j
                s_idx = self.n * (i + 1) + j
                e_idx = self.n * i + j + 1

                if self.matrix[i][j] != '#':
                    if i + 1 < self.m:
                        self.g[idx][s_idx] = int(self.matrix[i + 1][j])

                    if j + 1 < self.n:
                        self.g[idx][e_idx] = int(self.matrix[i][j + 1])

                if self.matrix[i][j] == 'W' and j - 1 >= 0:
                    w_idx = self.n * i + j - 1
                    self.g[idx][w_idx] = 0

                if self.matrix[i][j] == 'N' and i - 1 >= 0:
                    n_idx = self.n * (i - 1) + j
                    self.g[idx][n_idx] = 0

        return self.g

    def convert_idx_to_trace(self, idx_trace: List[int]) -> List[tuple]:

        res = []

        for idx in idx_trace:
            i = idx // self.n
            j = idx - (i * self.n)

            res.append((i, j))

        return res


class StrongComponentResolver:
    def __init__(self, g: List[Type[dict]], n: int):
        self.g = g
        self.n = n
        self.num: List[int] = [0 for _ in range(self.n)]
        self.low: List[int] = list(self.num)
        self.time: int = 0
        self.state: List[int] = [0 for _ in range(self.n)]
        self.s: deque = deque()
        self.free: List[int] = [True for _ in range(self.n)]
        self.scc: defaultdict = defaultdict(list)

        self.order_time = -1
        self.scc_tree: defaultdict = defaultdict(set)
        self.related_scc: List[set] = [set() for _ in range(self.n)]
        self.num_scc: List[int] = [0 for _ in range(self.n)]

    def dfs_build(self, u: int, p: int):
        self.state[u] = 1
        self.time += 1
        self.low[u] = self.num[u] = self.time
        self.s.append(u)
        for v in self.g[u]:
            if v == p or self.state[v] == 2:
                continue
            if self.state[v] == 1:
                self.low[u] = min(self.low[u], self.num[v])
                continue
            self.dfs_build(v, u)
            if self.free[v]:
                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.related_scc[u].add(self.num_scc[v])

        self.state[u] = 2
        if self.low[u] == self.num[u]:
            self.order_time += 1
            v = self.s.pop()
            while self.s and v != u:
                self.free[v] = False
                self.num_scc[v] = self.order_time
                self.scc[self.order_time].append(v)
                self.scc_tree[self.order_time].union(self.related_scc[v])
                v = self.s.pop()

            self.scc[self.order_time].append(v)
            self.scc_tree[self.order_time].union(self.related_scc[v])
            self.free[v] = False

    def resolve(self):
        self.s.clear()

        for u in range(self.n):
            if self.state[u] == 0:
                self.dfs_build(u, -1)


class TopologicalSort:
    def __init__(self, g: defaultdict, n: int):
        self.n = n
        self.g: defaultdict = defaultdict(list)

        for u in g.keys():
            self.g[u] = list(g[u])

        self.in_degrees: defaultdict = defaultdict(int)

    def initialize(self):

        for u in self.g.keys():
            for v in self.g[u]:
                self.in_degrees[v] += 1

    def solve(self) -> List[int]:

        orders: List[int] = []

        q: deque = deque()
        self.initialize()
        for u in self.in_degrees.keys():
            if self.in_degrees[u] == 0:
                q.append(u)

        while q:
            u = q.popleft()
            orders.append(u)

            for v in self.g[u]:
                self.in_degrees[v] -= 1
                if self.in_degrees[v] <= 0:
                    q.append(v)

        return orders


class KCollectSolution:
    def __init__(self, raw_inp: str, n: int, m: int):
        self.adapter = KCollectAdapter(m, n, raw_inp)

        self.g: List[Type[dict]] = self.adapter.build()
        self.m: int = m
        self.n: int = n

    def solve(self, ) -> int:

        scc_resolver: StrongComponentResolver = StrongComponentResolver(self.g, self.n * self.m)

        scc_resolver.resolve()

        scc_tree: defaultdict = scc_resolver.scc_tree
        num_scc = scc_resolver.order_time + 1
        nodes_of_scc: defaultdict = scc_resolver.scc

        orders: List[int] = TopologicalSort(scc_tree, num_scc).solve()
        weights: List[int] = []
        begin = 0

        in_deg = defaultdict(list)
        for u in scc_tree.keys():
            for v in scc_tree[u]:
                in_deg[v].append(u)

        for idx, scc_id in enumerate(orders):
            weights.append(self.calc_weight(scc_id, nodes_of_scc))
            if 0 in nodes_of_scc[scc_id]:
                begin = idx
        max_return = -1
        dp = defaultdict(int)
        traces: defaultdict = defaultdict(lambda: -1)
        end_id = -1
        for i in range(begin, len(orders)):
            scc_id = orders[i]
            near_scc = in_deg[scc_id]
            max_scc = 0
            prev_scc_id = 0
            for in_near in near_scc:
                if dp[in_near] > max_scc:
                    max_scc = dp[in_near]
                    prev_scc_id = in_near

            dp[scc_id] += max_scc + weights[i]
            traces[scc_id] = prev_scc_id
            if dp[scc_id] > max_return:
                max_return = dp[i]
                end_id = scc_id
        path_scc_id = [end_id]

        while traces[end_id] != -1:
            end_id = traces[end_id]
            path_scc_id.insert(0, end_id)

        return max_return

    def calc_weight(self, scc_id: int, nodes_of_scc: defaultdict) -> int:

        nodes = nodes_of_scc[scc_id]

        weight = 0
        n = len(nodes)
        for i in range(n):
            for j in range(i + 1, n):
                weight += self.g[nodes[i]][nodes[j]]
                weight += self.g[nodes[i]][nodes[j]]

        return weight
