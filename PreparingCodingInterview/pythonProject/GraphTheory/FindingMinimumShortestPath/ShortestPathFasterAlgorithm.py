from typing import List, Deque
from collections import deque

inf = 10 ** 9 + 7


class TargetEdge:
    def __init__(self, v: int, c: int):
        self.v: int = v
        self.c: int = c


class SPFASolution:
    def __init__(self, m: int, n: int, s: int, g: List[List[TargetEdge]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[TargetEdge]] = g
        self.s: int = s

    def solve(self) -> List[int] | None:

        dist: List[int] = [inf for _ in range(self.n + 1)]
        cnt: List[int] = [0 for _ in range(self.n + 1)]
        in_queue: List[bool] = [False for _ in range(self.n + 1)]

        q: Deque[int] = deque()

        dist[self.s] = 0
        in_queue[self.s] = True
        q.append(self.s)

        while q:
            u: int = q.popleft()
            in_queue[u] = False

            for e in self.g[u]:

                if dist[u] + e.c < dist[e.v]:
                    dist[e.v] = dist[u] + e.c

                    if not in_queue[e.v]:
                        q.append(e.v)

                        in_queue[e.v] = True
                        cnt[e.v] += 1

                        if cnt[e.v] > self.n:
                            return None

        return dist
