from typing import List, Tuple
import functools as ftool
import itertools as looptool




class CountingPathOnDAGSolution:
    def __init__(self, n_node: int, m_edge: int, edges: List[Tuple[int, int]]):

        self.n_node = n_node
        self.m_edge = m_edge
        self.edges: List[Tuple[int, int]] = edges

    def solve(self) -> List[int]:

        g: List[List[int]] = [[] for _ in range(self.n_node)]

        for uid, vid in self.edges:
            g[uid].append(vid)

        visited: List[bool] = [False] * self.n_node
        n_topo = -1
        beg: List[int] = [0] * self.n_node
        def dfs(u: int):
            nonlocal n_topo
            visited[u] = True

            for v in g[u]:
                if not visited[v]:
                    dfs(v)

            n_topo += 1
            beg[n_topo] = u

        for i in range(self.n_node):
            if not visited[i]:
                dfs(i)

        topo_order = list(reversed(beg))

        dp: List[int] = [0] * self.n_node

        dp[0] = 1

        for iid in range(self.n_node):
            uid = topo_order[iid]
            for vid in g[uid]:
                dp[vid] += dp[uid]

        return dp