from typing import List, Tuple


class MinReorderSolution:

    def __init__(self, n: int, connections: List[List[int]]):
        self.n: int = n
        self.connections: List[List[int]] = connections

        self.g: List[List[Tuple[int, bool]]] = [[] for _ in range(self.n)]
        self.num_reorder: int = 0
        self.reach_zero: List[bool] = [False] * n

    def solve(self) -> int:
        for conn in self.connections:
            u, v = conn
            self.g[u].append((v, False))
            self.g[v].append((u, True))

        self.dfs_solve(0)
        return self.num_reorder

    def dfs_solve(self, u: int, p: int = -1):

        for v, is_inverted in self.g[u]:
            if v == p:
                continue
            if not is_inverted:
                self.num_reorder += 1

            self.dfs_solve(v, u)


n1, connections1 = 5, [[1,0],[1,2],[3,2],[3,4]]

sln = MinReorderSolution(n1, connections1)

print(sln.solve())
