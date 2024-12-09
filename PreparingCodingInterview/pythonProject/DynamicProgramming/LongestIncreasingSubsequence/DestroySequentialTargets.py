from typing import List, DefaultDict
from collections import defaultdict


class DestroySequentialTargetSolution:
    def __init__(self, nums: List[int], space: int):
        self.nums: List[int] = nums
        self.space: int = space

    def solve(self) -> int:

        freq_mod: DefaultDict[int, List[int]] = defaultdict(lambda: [10 ** 9 + 7, 0])

        max_freq = -1
        min_num = 10 ** 9 + 7

        for num in self.nums:
            mod_space = num % self.space
            min_in_mod, num_mod = freq_mod[mod_space]
            if num < min_in_mod:
                min_in_mod = num
            freq_mod[mod_space][0], freq_mod[mod_space][1] = min_in_mod, num_mod + 1

            if num_mod + 1 > max_freq:
                min_num = min_in_mod
                max_freq = num_mod + 1
            elif num_mod + 1 == max_freq and min_in_mod < min_num:
                min_num = min_in_mod

        return min_num


nums1 = [3,7,8,1,1,5]
space1 = 2

sln = DestroySequentialTargetSolution(nums1, space1)

print(sln.solve())
