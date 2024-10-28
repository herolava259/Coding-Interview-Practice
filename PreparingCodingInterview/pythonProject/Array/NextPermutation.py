from typing import List


class NextPermutationSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> None:

        n = len(self.nums)

        cur_p = n-1

        while cur_p > 0 and self.nums[cur_p-1] >= self.nums[cur_p]:
            cur_p -= 1

        if cur_p == 0:
            first_p, last_p = 0, n - 1

            while first_p < last_p:
                self.nums[first_p], self.nums[last_p] = self.nums[last_p], self.nums[first_p]
                first_p += 1
                last_p -= 1
            return
        cd_p = cur_p-1

        cur_p = n-1

        while cur_p > cd_p and self.nums[cur_p] <= self.nums[cd_p]:
            cur_p -= 1

        self.nums[cur_p], self.nums[cd_p] = self.nums[cd_p], self.nums[cur_p]

        first_p, last_p = cd_p+1, n-1

        while first_p < last_p:
            self.nums[first_p], self.nums[last_p] = self.nums[last_p], self.nums[first_p]
            first_p += 1
            last_p -= 1

        return
