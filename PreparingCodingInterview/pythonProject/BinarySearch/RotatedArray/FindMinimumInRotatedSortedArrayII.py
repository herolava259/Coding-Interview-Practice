from typing import List

class FindMinimumSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:

        def calc_pivot_point(f: int, l: int)-> int:
            return (f + l) >> 1 #+ ((f + l) & 1)


        seq_contain_two_part = lambda fv, lv, pv: (pv >= fv >= lv or pv <= lv <= fv )

        seq_contain_only_once = lambda fv, lv, pv: fv <= pv <= lv

        low, high = 0, len(self.nums)-1

        # find k first elements of array

        while self.nums[low] == self.nums[high] and low < high:
            low += 1

        while low < high:
            pivot_point = calc_pivot_point(low, high)

            f_val, l_val, p_val = self.nums[low], self.nums[high], self.nums[pivot_point]

            if seq_contain_only_once(f_val, l_val, p_val):
                break

            if seq_contain_two_part(f_val, l_val, p_val):
                if p_val > l_val: # case: pivot point's in last n-k elements of the array
                    low = pivot_point + 1
                else: # case: pivot point's in first k elements
                    high = pivot_point

        return self.nums[low]


nums1: List[int] = [3,3,1,3]

sln = FindMinimumSolution(nums1)
print(sln.solve())



