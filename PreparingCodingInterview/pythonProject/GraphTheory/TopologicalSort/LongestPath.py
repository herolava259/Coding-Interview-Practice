from typing import List


class TopologicalSortSolution:

    def __init__(self, g: List[List[int]]):

        self.g: List[List[int]] = g
        self.n: len(g)
        self.states: List[int] = [0 for _ in range(self.n + 1)]

        self.orders: List[int] = []

    def dfs_solve(self, u: int) -> bool:

        self.states[u] = 1

        for v in self.g[u]:
            if self.states[v] == 1:
                return False
            if self.states[v] == 2:
                continue
            if self.states[v] == 0:
                if not self.dfs_solve(v):
                    return False

        self.orders.append(u)
        self.states[u] = 2
        return True

    def solve(self) -> List[int] | None:

        for u in range(self.n + 1):
            if self.states[u] == 0:
                if not self.dfs_solve(u):
                    return None

        return self.orders[::-1]

class LongestPathSolution:
    def __init__(self, n: int, g: List[List[int]]):

        self.n: int = n
        self.g: List[List[int]] = g
        self.topo_sln = TopologicalSortSolution(g)

    def solve(self) -> int:
        dp = [1 for _ in range(self.n + 1)]
        orders: List[int] | None = self.topo_sln.solve()
        if orders is None :
            return -1

        max_dp = -1

        for u in orders[::-1]:
            tmp_dp = -1

            for v in self.g[u]:
                if tmp_dp < dp[v]:
                    tmp_dp = dp[v]
            dp[u] = tmp_dp + 1

            if dp[u] > max_dp:
                max_dp = dp[u]

        return max_dp


