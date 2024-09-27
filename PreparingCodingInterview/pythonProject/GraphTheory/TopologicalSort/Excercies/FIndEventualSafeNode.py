from typing import List


class EventualSafeNodeSolution:
    def __init__(self, graph: List[List[int]]):

        self.g: List[List[int]] = graph
        self.n: int = len(self.g)
        self.visited: List[bool] = [False] * self.n
        self.is_safe: List[bool] = [False] * self.n

    def dfs_build(self, u: int) -> bool:

        if self.visited[u]:
            return self.is_safe[u]
        is_safe = True
        self.visited[u] = True
        if not self.g[u]:
            self.is_safe[u] = True
            return True

        for v in self.g[u]:
            is_safe &= self.dfs_build(v)

        self.is_safe[u] = is_safe

        return is_safe

    def solve(self) -> List[int]:

        for u in range(self.n):
            if not self.visited[u]:
                _ = self.dfs_build(u)

        return list(filter(lambda e: self.is_safe[e], range(self.n)))


g1 = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]

sln = EventualSafeNodeSolution(g1)

print(sln.solve())
