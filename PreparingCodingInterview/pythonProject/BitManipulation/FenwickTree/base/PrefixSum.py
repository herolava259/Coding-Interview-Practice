from typing import List


class FenwickTree4PrefixSum:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr
        self.n: int = len(arr)
        self.bit: List[int] = [0] * self.n

    def update(self, idx: int, v: int):
        while idx <= self.n:
            self.bit[idx] += v
            idx += idx & (-idx)

    def update_range(self, beg_idx: int, end_idx: int, v: int):
        self.update(beg_idx, v)
        self.update(end_idx+1, -v)


    def initialize(self):

        for idx, u in enumerate(self.arr):
            self.update(idx, u)

    def query_prefix_sum(self, length: int) -> int:
        ans = 0
        idx = length - 1

        if idx < 0:
            return 0
        while idx > 0:
            ans += self.bit[idx]
            idx -= idx & (-idx)
        return ans

    def query_range(self, beg_idx: int, end_idx: int) -> int:
        return self.query_prefix_sum(end_idx + 1) - self.query_prefix_sum(beg_idx)


