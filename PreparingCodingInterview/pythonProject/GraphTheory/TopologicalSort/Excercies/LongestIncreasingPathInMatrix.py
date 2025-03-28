from typing import List, Deque as Queue
from collections import deque as queue


class LongestIncreasingPathSolution:
    def __init__(self, matrix: List[List[int]]):

        self.matrix: List[List[int]] = matrix

    def solve(self) -> int:
        m, n = len(self.matrix), len(self.matrix[0])
        def build_graph() -> List[List[int]]:

            nonlocal m, n

            len_g = m * n
            graph: List[List[int]] = [[] for _ in range(len_g)]

            for i in range(m):
                for j in range(n):
                    cell_ij = self.matrix[i][j]
                    nxt_i, nxt_j = i+1, j+1
                    if nxt_i < m:
                        cell_nxt = self.matrix[nxt_i][j]
                        if cell_ij < cell_nxt:
                            graph[i*n + j].append(nxt_i*n + j)
                        elif cell_ij > cell_nxt:
                            graph[nxt_i*n + j].append(i*n + j)

                    if nxt_j < n:
                        cell_nxt = self.matrix[i][nxt_j]

                        if cell_ij < cell_nxt:
                            graph[i*n + j].append(i*n + nxt_j)
                        elif cell_ij > cell_nxt:
                            graph[i*n + nxt_j].append(i*n + j)
            return graph

        num_v = m*n
        g: List[List[int]] = build_graph()

        def topo_sort()-> List[int]:
            in_deg: List[int] = [0] * num_v
            order: List[int] = []
            for u in range(num_v):
                for v in g[u]:
                    in_deg[v] += 1

            q: Queue[int] = queue()

            for u, deg in enumerate(in_deg):
                if deg == 0:
                    q.append(u)
                    order.append(u)

            while q:
                u = q.popleft()

                for v in g[u]:
                    in_deg[v] -= 1

                    if in_deg[v] == 0:
                        q.append(v)
                        order.append(v)

            return order

        priority: List[int] = topo_sort()

        dp: List[int] = [1] * num_v
        max_dp = 1

        for uid in reversed(priority):

            for vid in g[uid]:
                dp[uid] = max(dp[vid]+1, dp[uid])

            max_dp = max(dp[uid], max_dp)

        return max_dp


matrix1 = [[9,9,4],[6,6,8],[2,1,1]]

print(LongestIncreasingPathSolution(matrix1).solve())

