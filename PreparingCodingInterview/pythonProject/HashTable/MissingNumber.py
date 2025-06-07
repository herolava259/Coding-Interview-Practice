from typing import List

class MissingNumberSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:

        n = len(self.nums) + 1

        total = n*(n-1) // 2

        return total - sum(self.nums)
    def xor_solve(self) -> int:

        xor_total = 0

        for num in range(len(self.nums)+1):
            xor_total ^= num

        for num in self.nums:
            xor_total ^= num

        return xor_total

print(MissingNumberSolution([9,6,4,2,3,5,7,0,1]).xor_solve())