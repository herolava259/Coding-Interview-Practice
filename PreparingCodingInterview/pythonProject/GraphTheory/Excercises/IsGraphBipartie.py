from typing import List


class IsBipartiteSolution:
    def __init__(self, g: List[List[int]]):
        self.g: List[List[int]] = g

    def solve_by_dfs(self) -> bool:

        n = len(self.g)
        colors: List[int] = [-1] * n

        def dfs_paint(u: int, set_color: int = 0) -> bool:

            colors[u] = set_color
            opposite_color = 1 - set_color

            for v in self.g[u]:
                if colors[v] > -1:
                    if colors[v] != opposite_color:
                        return False
                    continue
                check = dfs_paint(v, opposite_color)
                if not check:
                    return False

            return True

        for u in range(n):
            if colors[u] > -1:
                continue
            flag = dfs_paint(u)

            if not flag:
                return False

        return True


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

sln = IsBipartiteSolution(graph)

print(sln.solve_by_dfs())
