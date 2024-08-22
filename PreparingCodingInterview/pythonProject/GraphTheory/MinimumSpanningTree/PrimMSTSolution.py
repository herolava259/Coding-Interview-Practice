from typing import List
from DisjoinSetUnion import Edge
import heapq

max_value = 100_000_007


class PrimMSTSolution:
    def __init__(self, g: List[List[tuple]], n: int):
        self.n = n
        self.g = g

    def solve(self) -> (int, List[Edge]):

        priority_queue, s = [], 0

        priority_queue.append((s, s, 0))

        total_w, mst = 0, []

        visited = [False for _ in range(self.n + 1)]
        dv: List[int] = [max_value for _ in range(self.n)]

        while priority_queue:
            u, v, d = heapq.heappop(priority_queue)

            if visited[u] and visited[v]:
                continue

            visited[u] = visited[v] = True
            total_w += d
            if u != v:
                mst.append(Edge(u, v, d))

            for p, c in self.g[v]:
                if not visited[v] and c < dv[p]:
                    heapq.heappush(priority_queue, (v, p, c))
                    dv[p] = c

        return total_w, mst
