from typing import List


class LargestPathValueSolution:
    def __init__(self, colors: str, edges: List[List[int]]):

        self.colors: str = colors
        self.edges: List[List[int]] = edges
        self.n: int = len(colors)

    def topological_sort(self) -> List[int] | None:
        states: List[int] = [0] * self.n
        g: List[List[int]] = [[] for _ in range(self.n)]
        orders: List[int] = []

        for u, v in self.edges:
            g[u].append(v)

        def dfs_find(u_n: int) -> bool:
            states[u_n] = 1

            for v_n in g[u_n]:
                if states[v_n] == 2:
                    continue
                elif states[v_n] == 1:
                    return False

                if not dfs_find(v_n):
                    return False

            orders.insert(0, u_n)
            states[u_n] = 2
            return True

        for u in range(self.n):
            if states[u] == 0:
                if not dfs_find(u):
                    return None

        return orders

    def solve(self) -> int:

        orders: List[int] | None = self.topological_sort()

        if not orders:
            return -1
        in_g: List[List[int]] = [[] for _ in range(self.n)]
        dp: List[List[int]] = [[0] * 26 for _ in range(self.n)]

        for u, v in self.edges:
            in_g[v].append(u)

        jdxs: List[int] = [ord(c)-97 for c in set(self.colors)]
        max_dp = 0

        for u in orders:

            jdx = ord(self.colors[u]) - 97
            for in_u in in_g[u]:
                for j in jdxs:
                    dp[u][j] = max(dp[u][j], dp[in_u][j])

            dp[u][jdx] += 1

            if dp[u][jdx] > max_dp:
                max_dp = dp[u][jdx]

        return max_dp


colors1 = "aa"
edges1 = [[0,1],[1, 0]]

sln = LargestPathValueSolution(colors1, edges1)

print(sln.solve())
