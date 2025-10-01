from typing import List, Deque, Tuple
from collections import deque

class ShortestPathLengthSolution:
    def __init__(self, graph: List[List[int]]):
        self.g: List[List[int]] = graph

    def solve(self) -> int:
        n = len(self.g)

        max_path = 17 #10 ** 9 + 7
        dp: List[List[int]] = [[max_path] * n for _ in range(1<<n)]

        q: Deque[Tuple[int, int]] = deque()

        for u in range(n):
            dp[1 << u][u] = 0
            q.append((u, 1<< u))
        terminated_msk = (1 << n) - 1

        while q:
            u, msk = q.popleft()

            if msk == terminated_msk:
                continue

            for v in self.g[u]:
                nxt_msk = msk | (1 << v)
                if dp[nxt_msk][v] > dp[msk][u] + 1:
                    dp[nxt_msk][v] = dp[msk][u] + 1
                    q.append((v, nxt_msk))

        return min(dp[-1][u] for u in range(n))


if __name__ == "__main__":
    graph = [[1,2,3,4],[0,2],[0,1],[0,5],[0,6],[3],[4]]
    print(ShortestPathLengthSolution(graph).solve())
