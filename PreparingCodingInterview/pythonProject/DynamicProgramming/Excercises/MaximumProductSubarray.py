from typing import List


class MaxProductSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:
        dp_last_max = self.nums[0]
        dp_last_min = dp_last_max
        max_product = dp_last_min

        for item in self.nums[1:]:
            tmp_last_min, tmp_last_max = dp_last_min, dp_last_max
            dp_last_max = max(item, tmp_last_min * item, tmp_last_max * item)
            dp_last_min = min(item, tmp_last_max * item, tmp_last_min * item)

            max_product = max(max_product, dp_last_max)

        return max_product


nums = [-4,-3,-2]

sln = MaxProductSolution(nums)

print(sln.solve())
