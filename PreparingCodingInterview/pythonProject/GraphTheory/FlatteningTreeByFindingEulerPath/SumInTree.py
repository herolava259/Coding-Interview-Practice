from typing import List
from BuildingEulerPathInTree import SimpliedBuildingEulerPathInTree


class Node:
    def __init__(self, nid: int, val: int, parent, childs: list | None = None):
        self.nid = nid
        self.val = val
        self.par = parent
        self.childs: list = childs if childs is not None else []

    def change(self, val: int):
        self.val = val


class NaiveSumInTreeSolution:
    def __init__(self, g: List[List[int]], values: List[int], parents: List[int], n: int, m: int):
        self.num_node = n
        self.num_edge = m
        self.parents: List[int] = parents
        self.g = g
        self.values = values

    def change(self, u: int, val: int) -> None:
        self.values[u] = val

    def sum(self, u: int) -> int:
        s: int = self.values[u]

        for v in self.g[u]:
            if v != self.parents[u]:
                s += self.sum(v)


class FenwickTreeSolution:
    def __init__(self, g: List[List[int]], values: List[int], n: int, m: int):
        self.num_node = n
        self.num_edge = m
        self.values = values
        self.g = g
        self.bit: List[int] = [0 for _ in range(n + 1)]
        self.euler_sln = SimpliedBuildingEulerPathInTree(n, m, g)
        self.st: List[int] = []
        self.en: List[int] = []
        self.tour: List[int] = []

    def start(self):
        self.tour = self.euler_sln.solve()
        self.st = self.euler_sln.starts
        self.en = self.euler_sln.ends

    def sum_prefix(self, i: int) -> int:
        ans: int = 0

        while i >= 0:
            ans += self.bit[i]
            i &= i - 1

        return ans

    def add(self, i: int, x: int):
        while i <= self.num_node:
            self.bit[i] += x
            i += i & (-i)

    def sum_sub_tree(self, u: int) -> int:
        return self.sum_prefix(self.en[u]) - self.sum_prefix(self.st[u] - 1)

    def command(self, u: int, x: int) -> None:
        i = self.st[u]
        self.add(i, x)

    def query(self, u: int) -> int:
        return self.sum_sub_tree(u)



