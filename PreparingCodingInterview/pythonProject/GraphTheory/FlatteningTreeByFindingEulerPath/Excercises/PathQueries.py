from typing import List



class FlatteningTreeResolver:

    def __init__(self, n: int, root: int, tree: List[List[int]], weights: List[int]):
        self.n: int = n
        self.root: int = root
        self.tree: List[List[int]] = tree
        self.st: List[int] = [0 for _ in range(self.n+1)]
        self.en: List[int] = [0 for _ in range(self.n+1)]

        self.beg_roots: List[int] = [0 for _ in range(self.n+1)]
        self.time: int = 0
        self.parents: List[int] = [0 for _ in range(self.n+1)]
        self.weights: List[int] = weights
        self.tour: List[int] = []

    def dfs_build(self, u: int, p: int = -1):

        self.parents[u] = p
        self.add_tour(u, self.weights[u])
        self.st[u] = self.time
        if u != self.root:
            self.beg_roots[u] = self.en[self.root] - 1

        for v in self.tree[u]:
            if v != p:
                self.dfs_build(v, u)
                if u == self.root:
                    self.add_tour(u, 0)
        self.en[u] = self.time

    def add_tour(self, u: int, val: int):
        self.time += 1
        self.en[u] = self.time
        self.tour.append(val)

    def resolve(self):
        self.dfs_build(self.root, -1)


class FenwickTreeSolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = list(arr)
        self.n: int = len(arr)

        self.bit_sum: List[int] = [0 for _ in range(self.n)]

    def build(self):

        for i in range(self.n):
            self.bit_sum[i] = self.arr[i]
            end = i
            last_bit_val = end & (-end)
            beg = end - last_bit_val
            end -= 1
            while end > beg:
                self.bit_sum[i] = self.bit_sum[end]
                end &= end-1

    def add(self, idx: int, val: int):

        beg = idx

        while beg < self.n:
            self.bit_sum[beg] += val
            beg += beg & (-beg)

        self.arr[idx] += val

    def sum_prefix(self, end: int) -> int:

        sums = 0
        while end >= 0:
            sums += self.bit_sum[end]
            end &= (end - 1)

        return sums

    def sum(self, start_idx: int, end_idx: int) -> int:
        return self.sum_prefix(end_idx) - self.sum_prefix(start_idx - 1)


class PathQueriesSolution:
    def __init__(self, n: int, tree: List[List[int]], weights: List[int], root: int):

        self.n = n
        self.tree = tree
        self.weights = weights
        self.root = root
        self.flatten_tree = FlatteningTreeResolver(n, root, tree, weights)
        self.fenwick_tree : FenwickTreeSolution | None = None

    def initialize(self):

        self.flatten_tree.resolve()

        self.flatten_tree = FenwickTreeSolution(self.flatten_tree.tour)

    def command_add(self, s: int, x: int):
        idx = self.flatten_tree.st[s] - 1

        self.weights[s] += x
        self.fenwick_tree.add(idx, x)

    def query_sum(self, s: int) -> int:

        beg_idx = self.flatten_tree.beg_roots[s]
        end_idx = self.flatten_tree.st[s]

        return self.fenwick_tree.sum(beg_idx, end_idx)

