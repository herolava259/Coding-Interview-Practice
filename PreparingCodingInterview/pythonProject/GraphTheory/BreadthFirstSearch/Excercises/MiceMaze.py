from typing import List
import heapq


class TargetEdge:
    def __init__(self, v: int, c: int):
        self.v: int = v
        self.c: int = c


inf = 10 ** 9 + 7


class MiceMazeSolution:
    def __init__(self, n: int, end: int, t: int, dir_g: List[List[TargetEdge]]):
        self.n: int = n
        self.end: int = end
        self.t: int = t
        self.g: List[List[TargetEdge]] = dir_g

    def bfs_solve(self) -> int:
        q: List[tuple] = [(0, self.end)]
        dv: List[int] = [inf for _ in range(self.n + 1)]

        while not q:
            min_d, u = heapq.heappop(q)

            for t_e in self.g[u]:
                if min_d + t_e.c > dv[t_e.v]:
                    dv[t_e.v] = min_d + t_e.c
                    heapq.heappush(q, (dv[t_e.v], t_e.v))

        num_pass = 0

        for u in range(1, self.n + 1):
            if u == self.end:
                continue
            if dv[u] <= self.t:
                num_pass += 1

        return num_pass
