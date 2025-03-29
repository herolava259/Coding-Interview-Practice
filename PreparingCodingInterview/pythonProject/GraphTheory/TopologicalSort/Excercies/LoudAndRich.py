from typing import List, Deque as Queue
from collections import deque as queue


class LoudAndRichSolution:
    def __init__(self, richer: List[List[int]], quiet: List[int]):

        self.richer: List[List[int]] = richer
        self.quiet: List[int] = quiet

    def solve(self) -> List[int]:

        n = len(self.quiet)

        g: List[List[int]] = [[] for _ in range(n+1)]

        in_deg: List[int] = [0] * n

        for u, v in self.richer:
            g[u].append(v)
            in_deg[v] += 1

        def topo_sort() -> List[int]:
            q: Queue[int] = queue()
            order: List[int] = []
            for uid, deg in enumerate(in_deg):
                if deg == 0:
                    q.append(uid)
                    order.append(uid)

            while q:
                uid = q.popleft()

                for vid in g[uid]:
                    in_deg[vid] -= 1

                    if in_deg[vid] == 0:
                        q.append(vid)
                        order.append(vid)
            return order

        priority: List[int] = topo_sort()

        result: List[int] = list(range(n))

        for u in priority:

            q_u = result[u]

            for v in g[u]:

                q_v = result[v]

                # if q_v == v:
                #     result[v] = q_u
                #     continue
                if self.quiet[q_u] < self.quiet[q_v]:
                    result[v] = q_u

        return result


richer = []
quiet = [0]

sln = LoudAndRichSolution(richer, quiet)

print(sln.solve())