from typing import List, Tuple
import math
from collections import deque
class FroggerSolution:
    def __init__(self, n: int, positions: List[Tuple[float, float]]):

        self.n: int = n
        self.positions: List[Tuple[float, float]] = positions

    def solve(self) -> float:

        s = self.positions[0]

        min_dist: List[float] = [1000000.0 for _ in range(self.n)]

        in_queue: List[bool] = [False for _ in range(self.n)]

        cnt: List[int] = [0 for _ in range(self.n)]

        q: deque = deque()

        q.append(0)
        in_queue[0] = True

        while q:
            u = q.popleft()

            in_queue[u] = False
            pos_u = self.positions[u]
            for v in range(self.n):
                if v == u:
                    continue
                pos_v = self.positions[v]
                new_dist = math.sqrt((pos_v[0]-pos_u[0]) ** 2 + (pos_v[1]-pos_u[1])**2)

                if min(new_dist, min_dist[u]) < min_dist[v]:
                    min_dist[v] = min(new_dist, min_dist[u])

                    if not in_queue[v]:
                        q.append(v)
                        in_queue[v] = True
                        cnt[v] += 1

                        if cnt[v] > self.n:
                            return -1.0

        return min_dist[1]


n1 = 2
positions1 = [(0, 0), (3, 4)]

sln = FroggerSolution(n1, positions1)

print(sln.solve())

