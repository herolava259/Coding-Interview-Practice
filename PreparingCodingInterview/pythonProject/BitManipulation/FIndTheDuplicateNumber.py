from typing import List
import math


class FindingDuplicateSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> List[int]:

        n = len(self.nums)
        ans = 0
        log2_n = math.ceil(math.log2(n))
        for i in reversed(range(math.ceil(n) + 1)):
            num_bit_one = 0
            num_cycle = n // (1 << i)
            num_cycle_one = num_cycle // 2

            num_one_time = num_cycle_one * (1 << i)

            if num_cycle % 2 == 1:
                num_one_time += n - num_cycle * (1 << i)

            for num in self.nums:

                cur_bit = (num >> i) & 1

                if cur_bit == 1:
                    num_bit_one += 1

            if num_bit_one > num_one_time:
                ans += 1 << i

        return ans


sln = FindingDuplicateSolution([1, 3, 4, 2, 2])

print(sln.solve())
