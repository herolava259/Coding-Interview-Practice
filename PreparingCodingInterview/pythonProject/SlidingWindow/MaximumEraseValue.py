from typing import List, Set, Dict

class MaximumUniqueSubarraySolution:
    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> int:

        size_nums = len(self.nums)

        max_val = 0
        cur_val = 0
        wd_vals: Set[int] = set()

        for idx in range(size_nums):
            if self.nums[idx] not in wd_vals:
                cur_val += self.nums[idx]
            else:
                max_val = max(max_val, cur_val)
                wd_vals.clear()
                cur_val = self.nums[idx]
            wd_vals.add(self.nums[idx])

        return max(max_val, cur_val)

    def hash_sd_solve(self) -> int:

        def accumulate_of(arr: List[int], fn,init_res: int = 0) -> List[int]:
            result: List[int] = [0] * len(arr)
            prev_res = init_res
            for ix, num in enumerate(arr):
                result[ix] = prev_res = fn(prev_res, num)
            return result

        acc_totals: List[int] = accumulate_of(self.nums, lambda a,b: a+b)
        acc_totals.append(0)

        inverse_map:Dict[int, int] = dict()
        cur_wd_size = 0
        max_total = 0
        max_size = len(self.nums)
        for idx in range(max_size):

            cur_val = self.nums[idx]
            beg_idx = idx - cur_wd_size

            cutting_idx = max(inverse_map.get(cur_val, beg_idx-1), beg_idx-1)

            cur_wd_total = acc_totals[idx] - acc_totals[cutting_idx]
            cur_wd_size = idx - cutting_idx
            max_total = max(max_total, cur_wd_total)
            inverse_map[cur_val] = idx

        return max_total

nums_test1 = [5,2,1,2,5,2,1,2,5]
nums_test2 = [4,2,4,5,6]

print(MaximumUniqueSubarraySolution(nums_test2).hash_sd_solve())
