import math
import os
import random
import re
import sys
from typing import List


class AtomicItem:
    def __init__(self, has_child, val_same, val_diff):
        self.has_child = has_child
        self.value_same = val_same
        self.value_diff = val_diff


class TimeRange:
    def __init__(self, beg: int, end: int):
        self.begin = beg
        self.end = end


mod_k = 100_000_007


class KingdomDivisionSolution:
    def __init__(self, n: int, roads: List[List[int]]):
        self.n = n
        self.roads = roads
        self.visited = [False for _ in range(n + 1)]
        self.time_ranges = [TimeRange(0, -1) for _ in range(n + 1)]
        self.time = 0
        self.dp = [AtomicItem(True, 0, 0) for _ in range(n + 1)]
        self.g: List[List[int]] = [[] for _ in range(n + 1)]
        self.root = 1

    def convert_adj_table(self) -> None:

        for r in self.roads:
            self.g[r[0]].append(r[1])
            self.g[r[1]].append(r[0])

    def dfs(self, u, p=0):

        self.visited[u] = True
        self.time += 1
        self.time_ranges[u].begin = self.time

        res_diff = 1
        res_same = 1
        num_child = len(self.g[u])
        if p != 0:
            num_child -= 1

        if u != self.root and len(self.g[u]) <= 1:
            self.dp[u].has_child = False
        else:
            self.dp[u].has_child = True
        is_leaf = not self.dp[u].has_child

        if is_leaf:
            res_diff = 0

        for v in self.g[u]:
            if v == p:
                continue
            if self.visited[v] and self.time_ranges[v].end == -1:
                continue
            if not self.visited[v]:
                self.dfs(v, u)
            res_same *= (self.dp[v].value_same + self.dp[v].value_diff)
            res_same %= mod_k

            res_diff = (res_diff * self.dp[v].value_diff) % mod_k

        self.time_ranges[u].end = self.time

        if not is_leaf:
            res_diff = (res_same - res_diff + mod_k) % mod_k

        self.dp[u].value_same = res_same
        self.dp[u].value_diff = res_diff

    def dfs_with_stack(self):
        s: List[int] = []
        s.append(self.root)
        p = 0
        counter = 0
        while counter < self.n:
            u = s[-1]
            self.atom_do(u)


    def atom_do(self, s: List[int], u: int):
        self.visited[u] = True
        self.time += 1
        self.time_ranges[u].begin = self.time

        num_child = len(self.g[u])
        if u != self.root:
            num_child -= 1

        if u != self.root and len(self.g[u]) <= 1:
            self.dp[u].has_child = False
        else:
            self.dp[u].has_child = True
        is_leaf = not self.dp[u].has_child

        if is_leaf:
            self.dp[u].value_diff = 0

        for v in self.g[u]:
            if v == p:
                continue
            if self.visited[v] and self.time_ranges[v].end == -1:
                continue
            if not self.visited[v]:
                s.append(v)

    def solve(self) -> int:
        self.convert_adj_table()
        self.dfs(self.root)

        res = (self.dp[self.root].value_diff * 2) % mod_k

        return res


def kingdomDivision(n, roads):

    sln = KingdomDivisionSolution(n, roads)
    return sln.solve()


inp1 = [[1, 2], [1, 3], [3, 4], [3, 5]]

inp2 = [[1, 2], [1, 5], [2, 3], [2, 4], [5, 6], [7, 5]]
n2 = 7

n1 = 5

inp3 = [[11, 2], [10, 5], [1, 6], [1, 7], [15, 8], [11, 9], [13, 11], [15, 12], [4, 13], [1, 4], [3, 1], [15, 14],
        [3, 15], [10, 3]]
n3 = 15
solution = KingdomDivisionSolution(n3, inp3)

print(solution.solve())
