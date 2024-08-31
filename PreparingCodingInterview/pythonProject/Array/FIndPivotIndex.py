from typing import List


class PivotIndexSolution:
    def __init__(self, nums: List[int]):

        self.nums = nums

    def solve(self) -> int:

        sum_nums = sum(self.nums)

        cur_sum = 0

        n = len(self.nums)

        for i in range(n):

            remain_nums = sum_nums - cur_sum - self.nums[i]

            if remain_nums == cur_sum:
                return i

            cur_sum += self.nums[i]

        return -1