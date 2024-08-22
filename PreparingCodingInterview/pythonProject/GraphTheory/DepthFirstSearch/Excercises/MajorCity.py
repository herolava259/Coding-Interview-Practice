from typing import List


class MajorCitySolution:
    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g

        self.num: List[int] = [0 for _ in range(n + 1)]
        self.low: List[int] = [0 for _ in range(n + 1)]
        self.tail: List[int] = [0 for _ in range(n + 1)]
        self.root: List[int] = [0 for _ in range(n + 1)]
        self.par: List[int] = [0 for _ in range(n + 1)]
        self.time: int = 0

        self.joint: List[bool] = [False for _ in range(n + 1)]

    def dfs_solve(self, u: int, p: int, root: int) -> int:

        self.root[u] = root
        self.par[u] = p
        self.time += 1
        self.num[u] = self.low[u] = self.time
        self.tail[u] += 1
        num_child = 0

        for v in self.g[u]:
            if v == p:
                continue
            if self.num[v] == 0:
                num_child += 1

                self.tail[u] += self.dfs_solve(v, u, root)
                self.low[u] = min(self.low[u], self.low[v])

                if num_child > 1 and u == root:
                    self.joint[u] = True
                elif self.low[v] > self.num[u]:
                    self.joint[u] = True
            else:
                self.low[u] = min(self.low[u], self.num[v])

        return self.tail[u]

    def build(self):
        for u in range(1, self.n + 1):
            if self.num[u] == 0:
                self.time = 0
                self.dfs_solve(u, 0, u)

    def solve(self) -> int:
        res = 0
        for u in range(1, self.n + 1):
            if self.joint[u]:
                root = self.root[u]
                p = self.par[u]

                total_childs: List[int] = []
                for v in self.g[u]:
                    if v == p:
                        continue
                    total_childs.append(self.tail[v])

                total_childs.append(self.tail[root] - self.tail[u])
                res += calc_num_couple(total_childs)
        return res


def calc_num_couple(dp: List[int]) -> int:
    total = 0
    elem_sq = 0
    for e in dp:
        total += e
        elem_sq += e ** 2

    return (total ** 2 - elem_sq) // 2
