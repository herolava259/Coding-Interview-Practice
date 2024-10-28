from typing import List


class SortColorsSolution:
    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> None:

        color_pieces = [0, 0, 0]

        for c in self.nums:
            color_pieces[c] += 1

        cur_p = 0

        for idx, n_c in enumerate(color_pieces):
            for i in range(n_c):
                self.nums[cur_p] = idx
                cur_p += 1
