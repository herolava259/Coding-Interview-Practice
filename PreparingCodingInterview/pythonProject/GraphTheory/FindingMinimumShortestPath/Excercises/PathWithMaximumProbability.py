from typing import List, Tuple
import heapq

class MaxProbabilitySolution:
    def __init__(self, n: int, edges: List[List[int]],
                 success_prob: List[float], start_node: int, end_node: int):
        self.n: int = n
        self.edges: List[List[int]] = edges
        self.success_prob: List[float] = success_prob
        self.start_node: int = start_node
        self.end_node: int = end_node

    def solve(self) -> float:

        failure_score: List[float] = [1/prob if prob > 1e-9 else 1e9 + 7 for prob in self.success_prob]

        d: List[float] = [1e9+7] * self.n
        pq: List[Tuple[float, int]] = []
        mark: List[bool] = [False] * self.n
        m = len(self.edges)

        d[self.start_node] = 1.0
        mark[self.start_node] = True

        g: List[List[Tuple[int, float]]] = [[] for _ in range(self.n)]

        for i in range(m):
            u, v = self.edges[i]
            sc = failure_score[i]

            if u == self.start_node:
                d[v] = sc
                heapq.heappush(pq, (sc, v))
            elif v == self.start_node:
                d[u] = sc
                heapq.heappush(pq, (sc, u))

            g[u].append((v, sc))
            g[v].append((u, sc))

        while pq:
            sc, u = heapq.heappop(pq)

            if mark[u]:
                continue

            mark[u] = True

            ## loose path
            for v, v_sc in g[u]:
                if mark[v]:
                    continue
                if d[u] * v_sc < d[v]:
                    d[v] = d[u] * v_sc
                    heapq.heappush(pq, (d[v], v))

        return round(1 / d[self.end_node], 8) if 1.0 <= d[self.end_node] < 1e9+7 else 0.0


n = 10
edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 5], [5, 6], [5, 7], [6, 8], [7, 9]]
succProb = [0.1, 0.2, 0.5, 0.6, 0.3, 0.7, 0.8, 0.9, 0.4, 0.5]
start = 0
end = 9

print(MaxProbabilitySolution(n, edges, succProb, start, end).solve())