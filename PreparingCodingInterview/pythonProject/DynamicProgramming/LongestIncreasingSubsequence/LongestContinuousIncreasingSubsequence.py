from typing import List

class LCISSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:

        cis_len = 1
        temp_len = 1
        n = len(self.nums)
        for i in range(1, n):
            if self.nums[i] > self.nums[i-1]:
                temp_len += 1
            else:
                temp_len = 1

            cis_len = max(temp_len, cis_len)

        return cis_len

nums1: List[int] = [2,2,2,2,2]

sln = LCISSolution(nums1)

print(sln.solve())