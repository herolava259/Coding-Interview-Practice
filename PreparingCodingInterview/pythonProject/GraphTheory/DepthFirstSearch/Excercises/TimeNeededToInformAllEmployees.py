from typing import List


class NumOfMinutesSolution:
    def __init__(self, n: int, headID: int, manager: List[int], informTime: List[int]):
        self.n: int = n
        self.head_id: int = headID
        self.manager: List[int] = manager
        self.inform_time: List[int] = informTime

    def build_tree(self) -> List[List[int]]:
        tree: List[List[int]] = [[] for _ in range(self.n)]

        for i in range(self.n):
            if self.manager[i] == -1:
                continue
            u, v = self.manager[i], i
            tree[u].append(v)

        return tree

    def solve(self) -> int:

        tree: List[List[int]] = self.build_tree()

        def dfs_max_minute(u: int) -> int:
            max_minute_time = 0

            for v in tree[u]:
                max_minute_time = max(max_minute_time, dfs_max_minute(v))

            return self.inform_time[u] + max_minute_time

        return dfs_max_minute(self.head_id)


n1 = 6
headID1 = 2
manager1 = [2, 2, -1, 2, 2, 2]
informTime1 = [0, 0, 1, 0, 0, 0]

sln = NumOfMinutesSolution(n1, headID1, manager1, informTime1)

print(sln.solve())
