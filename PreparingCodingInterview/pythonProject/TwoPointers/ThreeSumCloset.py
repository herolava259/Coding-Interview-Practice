from typing import List


class ThreeSumClosestSolution:
    def __init__(self, nums: List[int], target: int):

        self.nums: List[int] = nums

        self.target: int = target

    def solve(self) -> int:

        sorted_nums: List[int] = sorted(self.nums)


        closest_val = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]

        dist_target = lambda c : abs(c - self.target)

        for mid_p in range(1, len(sorted_nums) - 1):
            left_p, right_p = 0, len(sorted_nums) - 1

            while left_p < mid_p < right_p:
                cd_three_sum = sorted_nums[left_p] + sorted_nums[mid_p] + sorted_nums[right_p]

                if dist_target(cd_three_sum) < dist_target(closest_val):
                    closest_val = cd_three_sum

                if right_p == mid_p+1:
                    left_p += 1
                    continue
                if left_p == mid_p-1:
                    right_p -= 1
                    continue

                if cd_three_sum > self.target:
                    right_p -= 1
                elif cd_three_sum == self.target:
                    return self.target
                else:
                    left_p += 1

        return closest_val

nums1 = [-1,2,1,-4]

target1 = 1

sln = ThreeSumClosestSolution(nums1, target1)

print(sln.solve())

