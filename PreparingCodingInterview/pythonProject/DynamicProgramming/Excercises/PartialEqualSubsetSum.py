from typing import Set, List


class CanPartitionSolution:
    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> bool:

        sum_arr = sum(self.nums)

        if sum_arr % 2 == 1:
            return False

        dp: Set[int] = set()
        dp.add(self.nums[0])

        target_num = sum_arr // 2

        for num in self.nums[1:]:
            if target_num - num in dp:
                return True
            dp = dp.union([item + num for item in dp])

        return False


nums1 = [1,2,3,5]

sln = CanPartitionSolution(nums1)

print(sln.solve())
