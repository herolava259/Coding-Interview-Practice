from typing import List


class LongestSubArraySolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:

        cur_length, max_length = 0, 0

        first_idx = 0
        zero_idx = 0

        # if self.nums[0] == 0:
        #     first_idx = 0
        #     zero_idx = 0
        self.nums.append(0)
        self.nums.insert(0, 0)
        n = len(self.nums)

        for i in range(0, n):
            cur_val = self.nums[i]

            if cur_val == 1:
                continue
            max_length = max(max_length, i - first_idx - 1, 0)
            first_idx = zero_idx + 1
            zero_idx = i

        return max_length


nums1 = [1, 1, 0, 1, 0, 1, 1, 1]

sln = LongestSubArraySolution(nums1)

print(sln.solve())
