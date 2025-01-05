from typing import List


modk: int = 10**9 + 7

class NumberOfSubsequencesSolution:

    def __init__(self, nums: List[int], target: int):

        self.nums: List[int] = nums
        self.target: int = target

    def bs_solve(self) -> int:

        sorted_nums: List[int] = sorted(self.nums)

        num_sub_seq = 0
        n = len(self.nums)
        def bs_search(low: int = 0, high: int = n-1, supreme: int = 0) -> int:

            while low < high:
                mid = ((low + high ) >> 1) + ((low + high) & 1)

                if sorted_nums[mid] > supreme:
                    high = mid-1
                else:
                    low = mid

            return low

        if sorted_nums[0] * 2 > self.target:
            return 0

        num_sub_seq = 1
        prev_idx = 0
        for i in range(1, n):
            if sorted_nums[i] * 2 <= self.target:
                num_sub_seq = (num_sub_seq + (1 << i)) % modk
                prev_idx = i
                continue

            search_idx = bs_search(0, prev_idx, self.target - sorted_nums[i])
            if sorted_nums[i] + sorted_nums[search_idx] > self.target:
                break
            num_last_sub_seq = (((1 << (search_idx+1)) - 1) * (1 << (i - search_idx-1))) % modk
            num_sub_seq = (num_sub_seq + num_last_sub_seq) % modk
            prev_idx = search_idx

        return num_sub_seq

nums1 = [3,3,6,8]
target1 = 10

sln = NumberOfSubsequencesSolution(nums1, target1)

print(sln.bs_solve())
