from typing import List
import math


class RMQSolution:
    def __init__(self, arr: List[int], n: int):
        self.arr = arr
        self.n = n
        self.m1: List[List[int]] | None = None
        self.m2: List[int] | None = None
        self.infinity = 10 ** 9 + 7

    def init_solution_1(self):
        self.m1 = [[0] * self.n for _ in range(self.n)]

        for i in range(self.n):
            self.m1[i][i] = i

        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.arr[self.m1[i][j - 1]] < self.arr[j]:
                    self.m1[i][j] = self.m1[i][j - 1]
                else:
                    self.m1[i][j] = j

    def query_sln_1(self, i: int, j: int) -> tuple:
        if self.m1 is None:
            self.init_solution_1()

        return self.m1[i][j], self.arr[self.m1[i][j]]

    def init_solution_2(self):
        if self.m2 is not None:
            return

        sqrt_n = math.ceil(math.sqrt(self.n))
        len_part = int(math.sqrt(self.n))

        self.m2 = [0 for _ in range(sqrt_n)]

        for i in range(sqrt_n):

            beg = i * len_part
            end = min(self.n, beg + len_part)

            min_s = self.arr[beg]
            min_idx: int = beg
            for j in range(beg, end):
                if min_s > self.arr[j]:
                    min_s = self.arr[j]
                    min_idx = j
            self.m2[i] = min_idx

    def query_sln_2(self, i: int, j: int):
        self.init_solution_2()

        len_part = int(math.sqrt(self.n))

        beg_idx = i // len_part
        end_idx = j // len_part

        min_e = self.arr[i]
        arg_min = i
        if i < self.m2[beg_idx]:
            arg_min = self.m2[beg_idx]
            min_e = self.arr[arg_min]
        else:
            for k in range(i, (beg_idx + 1) * len_part):
                arg_min, min_e = self.compare_min(arg_min, min_e, k)

        for k in range(beg_idx + 1, end_idx - 1):
            if min_e > self.arr[self.m2[k]]:
                arg_min = self.m2[k]
                min_e = self.arr[arg_min]

        if i < self.m2[end_idx]:
            arg_min, min_e = self.compare_with_arg_min(arg_min, min_e, end_idx)
        else:
            for k in range(end_idx * len_part, j):
                arg_min, min_e = self.compare_with_arg_min(arg_min, min_e, k)

        return arg_min, min_e

    def compare_min(self, arg_min, min_e, idx) -> tuple:
        if min_e < self.arr[idx]:
            return idx, self.arr[idx]
        return arg_min, min_e

    def compare_with_arg_min(self, arg_min, min_e, idx) -> tuple:
        if min_e < self.arr[self.m2[idx]]:
            return self.m2[idx], self.arr[self.m2[idx]]
        return arg_min, min_e


class SparseTableRMQSolution:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.dp: List[List[int]] | None = None

    def build(self):

        sqrt_n = math.ceil(math.sqrt(self.n))

        self.dp = [[0 for _ in range(sqrt_n)] for i in range(self.n)]

        for i in range(self.n):
            self.dp[i][0] = i

        for j in range(1, sqrt_n):
            for i in range(self.n):
                if i + 1 << (j - 1) >= self.n:
                    self.dp[i][j] = self.dp[i][j - 1]
                elif self.arr[self.dp[i][j - 1]] <= self.arr[self.dp[i + 1 << (j - 1)][j - 1]]:
                    self.dp[i][j] = self.dp[i][j - 1]
                else:
                    self.dp[i][j] = self.dp[i + 1 << (j - 1) - 1][j - 1]

    def query(self, i: int, j: int) -> tuple:
        if self.dp is None:
            self.build()

        k = int(math.log(j - i + 1, 2))

        half_lower = self.arr[self.dp[i][k]]
        half_upper = self.arr[self.dp[j - 1 << k + 1][k]]

        if half_upper >= half_lower:
            return self.dp[i][k], half_lower
        else:
            return self.dp[j - 1 << k + 1][k], half_upper


def compare_min(id1: int, val1: int, id2: int, val2: int) -> tuple:
    if val1 <= val2:
        return id1, val1
    return id2, val2


class SegmentTreeRMQSolution:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.n = len(arr)
        self.st: List[int] | None = None
        self.infinity = 10 ** 9 + 7

    def build(self):

        self.st = [0 for _ in range(2 * self.n + 1)]
        self.initialize(1, 0, self.n - 1)

    def initialize(self, nid: int, first: int, last: int) -> tuple:

        if first == last:
            self.st[nid] = first
            return first, self.arr[first]

        mid = (first + last) // 2

        half_f_id, half_f_val = self.initialize(2 * nid, first, mid)
        half_l_id, half_l_val = self.initialize(2 * nid + 1, mid + 1, last)

        if half_f_val <= half_l_val:
            self.st[nid] = half_f_id
            return half_f_id, half_f_val
        else:
            self.st[nid] = half_l_id
            return half_l_id, half_l_val

    def query(self, nid: int, first: int, last: int, i: int, j: int) -> tuple:

        if i > last or j < first:
            return -1, self.infinity

        if i <= first <= last <= j:
            return self.st[nid], self.arr[self.st[nid]]

        mid = (first + last) // 2

        half_f_id, half_f_val = self.query(2 * nid, first, mid, i, j)
        half_l_id, half_l_val = self.query(2 * nid + 1, mid + 1, last, i, j)

        full_id, full_val = compare_min(half_f_id, half_f_val, half_l_id, half_l_val)

        return full_id, full_val
