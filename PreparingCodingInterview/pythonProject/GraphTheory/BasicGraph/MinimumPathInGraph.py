from typing import List
import heapq


class TargetEdge:
    def __init__(self, target: int, weight: int):
        self.target = target
        self.weight = weight


class Edge:
    def __init__(self, u: int, v: int, weight: int):
        self.u = u
        self.v = v
        self.weight = weight


infinity: int = 2 ** 31 - 1


class Path:
    def __init__(self, source, target, value: int = infinity):
        self.s = source
        self.tar = target
        self.value = value
        self.trace: List[int] = []


class BellmanFordSolution:

    def __init__(self, s: int, g: List[List[TargetEdge]]):
        self.s = s
        self.n = len(g) - 1
        self.m = 0
        self.g = g
        self.matrix: List[List[int]] = [[0 if i == j else infinity for j in range(self.n + 1)] for i in
                                        range(self.n + 1)]
        self.edges = []
        self.paths = [0 for _ in range(self.n + 1)]
        self.traces = [-1 for i in range(self.n + 1)]

        for u in range(1, self.n + 1):
            for e in self.g[u]:
                self.matrix[u][e.target] = e.weight
                self.m += 1
                self.edges.append(Edge(u, e.target, weight=e.weight))

    def solve(self) -> List[Path]:

        for i in range(1, self.n + 1):
            self.paths[i] = self.matrix[self.s][i]

        for i in range(self.m):
            for e in self.edges:
                self.loose_path(e)

        paths: List[Path] = []

        for u in range(1, self.n + 1):
            if self.s == u:
                paths.append(Path(u, u, 0))
            if self.paths[u] == infinity:
                paths.append(Path(self.s, u, value=infinity))
            else:
                path = Path(self.s, u, self.paths[u])
                path.trace = self.tracing(u)
        return paths

    def tracing(self, target: int) -> List[int]:

        path = []
        source = target
        i = 0
        while i < self.n and source != self.s:
            path.insert(0, source)
            source = self.traces[source]
            i += 1
        path.insert(0, self.s)

        return path

    def loose_path(self, edge: Edge):
        if self.paths[edge.v] > self.paths[edge.u] + edge.weight:
            self.paths[edge.v] = self.paths[edge.u] + edge.weight
            self.traces[edge.v] = edge.u


class DijikstraSolution:
    def __init__(self, s: int, g: List[List[TargetEdge]]):
        self.s = s
        self.n = len(g) - 1
        self.m = 0
        self.g = g
        self.matrix: List[List[int]] = [[0 if i == j else infinity for j in range(self.n + 1)] for i in
                                        range(self.n + 1)]
        self.edges = []
        self.paths = [(0, 0) for _ in range(self.n + 1)]
        self.dist = [infinity for _ in range(self.n + 1)]
        self.traces = [-1 for _ in range(self.n + 1)]
        self.frees = [True for _ in range(self.n + 1)]

        for u in range(1, self.n + 1):
            for e in self.g[u]:
                self.matrix[u][e.target] = e.weight
                self.matrix[e.target][u] = e.weight
                self.m += 1
                self.edges.append(Edge(u, e.target, weight=e.weight))

    def solve(self) -> List[Path]:

        res: List[Path] = []
        q: List[tuple] = []

        for i in range(1, self.n + 1):
            if i == self.s:
                self.dist[i] = 0
                continue
            q.append((self.matrix[self.s][i], i))
            self.dist[i] = self.matrix[self.s][i]
        heapq.heapify(q)

        while len(q) != 0:
            min_path = heapq.heappop(q)
            val, u = min_path
            if not self.frees[u]:
                continue
            self.frees[u] = False
            new_path = Path(self.s, u, val)
            new_path.trace = self.tracing(u)
            res.append(new_path)
            self.loose_path(u, val, q)
        return res

    def loose_path(self, u: int, val: int, q: List[tuple]):

        for ev in self.g[u]:
            if val + self.matrix[u][ev.target] < self.dist[ev.target]:
                self.dist[ev.target] = val + self.matrix[u][ev.target]
                self.traces[ev.target] = u
                heapq.heappush(q, (self.dist[ev.target], ev.target))

    def tracing(self, v) -> List[int]:

        u = v
        res = []
        while u != self.s:
            res.insert(0, u)
            u = self.traces[u]

        return res


class FloydWarshallSolution:
    def __init__(self, mtx: List[List[int]]):
        self.matrix = mtx
        self.num_node = len(mtx)
        self.trace = []
        for u in range(0, self.num_node + 1):
            trace_u: List[int] = [u for _ in range(0, self.num_node + 1)]
            self.trace.append(trace_u)

    def solve(self):
        dp: List[List[int]] = [[self.matrix[u][v] for v in range(self.num_node + 1)] for u in range(self.num_node + 1)]

        for k in range(1, self.num_node + 1):
            for u in range(1, self.num_node + 1):
                for v in range(1, self.num_node + 1):
                    if dp[u][v] > dp[u][k] + dp[k][v]:
                        dp[u][v] = dp[u][k] + dp[k][v]
                        self.trace[u][v] = k
