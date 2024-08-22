from typing import List
import math


class SparseTableRMQSolution:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.dp: List[List[int]] | None = None

    def initialize(self):
        if self.dp is not None:
            return
        log_n = int(math.log(self.n, 2))

        self.dp = [[0 for _ in range(log_n)] for _ in range(self.n)]

        for i in range(self.n):
            self.dp[i][0] = i

        for j in range(1, log_n + 1):
            for i in range(self.n):
                self.dp[i][j] = self.compute_min(i, j)

    def compute_min(self, i: int, log2_len: int):

        half_last_id = i + 1 << (log2_len - 1)

        if half_last_id >= self.n:
            half_last_id = self.n - (1 << (log2_len - 1))
        half_first = self.arr[self.dp[i][log2_len - 1]]
        half_last = self.arr[self.dp[half_last_id][log2_len - 1]]
        if half_first <= half_last:
            return self.dp[i][log2_len - 1]
        else:
            return self.dp[half_last_id][log2_len - 1]

    def query_min(self, i: int, j: int) -> tuple:

        log2_len_range = int(math.log(j - i + 1, 2))

        if self.arr[self.dp[i][log2_len_range]] <= self.arr[self.dp[i - 1 << log2_len_range][log2_len_range]]:
            return self.dp[i][log2_len_range], self.arr[self.dp[i][log2_len_range]]

        return self.dp[i - 1 << log2_len_range][log2_len_range], self.arr[self.dp[i - 1 << log2_len_range]
        [log2_len_range]]


class BuildingEulerPathInTree:
    def __init__(self, tree: List[List[int]], root: int):

        self.root: int = root
        self.tree: List[List[int]] = tree
        self.n: int = len(tree)

        self.h: List[int] | None = None
        self.tour_time: List[int] = []
        self.tour_node: List[int] = []
        self.time: int = 0
        self.parents: List[int] | None = None
        self.st: List[int] | None = None
        self.en: List[int] | None = None

    def dfs_build(self, u: int, p: int):

        if p != -1:
            self.h[u] = self.h[p] + 1
        self.parents[u] = p
        self.time += 1
        self.st[u] = self.time
        self.en[u] = self.time
        self.tour_time.append(self.st[u])
        self.tour_node.append(u)

        for v in self.tree[u]:
            if v != p:
                self.dfs_build(v, u)

        if p != -1:
            self.time += 1
            self.en[p] = self.time
            self.tour_time.append(self.st[p])
            self.tour_node.append(p)

    def initialize(self):
        self.h = [0 for _ in range(self.n + 1)]
        self.st = [0 for _ in range(self.n + 1)]
        self.en = [0 for _ in range(self.n + 1)]
        self.parents = [0 for _ in range(self.n + 1)]

        self.dfs_build(self.root, -1)


class CompanyQuerySolution:

    def __init__(self, tree: List[List[int]], root: int):
        self.tree = tree
        self.root = root
        self.euler_path_sln = BuildingEulerPathInTree(tree, root)
        self.rmq_query: SparseTableRMQSolution | None = None

    def build(self):
        self.euler_path_sln.initialize()
        self.rmq_query = SparseTableRMQSolution(self.euler_path_sln.tour_time)
        self.rmq_query.initialize()

    def query_lca(self, u: int, v: int) -> int:
        if self.euler_path_sln.en[u] > self.euler_path_sln.st[v]:
            u, v = v, u

        i = self.euler_path_sln.en[u] - 1
        j = self.euler_path_sln.st[v] - 1

        idx, _ = self.rmq_query.query_min(i, j)

        return self.euler_path_sln.tour_node[idx]
