from typing import List


class AllPathsSourceTargetSolution:
    def __init__(self, graph: List[List[int]]):

        self.g: List[List[int]] = graph
        self.n: int = len(self.g)

    def solve(self) -> List[List[int]]:

        paths: List[List[int]] = []

        def dfs_path(u: int, path: List[int]):

            path.append(u)
            if u == self.n - 1:
                paths.append(list(path))
                path.pop()
                return
            for v in self.g[u]:
                dfs_path(v, path)

            path.pop()

        dfs_path(0, [])
        return paths


graph1 = [[4,3,1],[3,2,4],[3],[4],[]]

sln = AllPathsSourceTargetSolution(graph1)

print(sln.solve())
