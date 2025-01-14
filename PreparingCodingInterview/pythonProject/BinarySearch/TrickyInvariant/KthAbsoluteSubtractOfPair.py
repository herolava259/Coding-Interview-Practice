from typing import List


class KthAbsSubtractPairSolution:
    def __init__(self, arr: List[int], k :int):
        self.arr: List[int] = arr
        self.k: int = k

    def solve(self) -> int:

        sorted_arr = sorted(self.arr)

        left, right = 0, len(sorted_arr)-1

        def min_diff(arr: List[int]) -> int:
            min_s = arr[1] - arr[0]

            for i in range(2, len(arr)):
                min_s = min(arr[i] - arr[i-1], min_s)
            return min_s

        def count_pairs_less_than_val(arr: List[int], upper_diff: int) -> int:
            num_pair = 0
            for i in range(0, len(arr)-1):
                low_idx, high_idx = i, len(arr)-1

                while low_idx < high_idx:
                    mid_idx = ((low_idx+high_idx) >> 1) + ((low_idx+high_idx) & 1)

                    if arr[mid_idx] - arr[i] >= upper_diff:
                        high_idx = mid_idx - 1
                    else:
                        low_idx = mid_idx

                num_pair += low_idx - i
            return num_pair



        low, high = min_diff(sorted_arr), sorted_arr[-1] - sorted_arr[0]

        while low < high:
            mid = ((low + high) >> 1) + ((low+high) & 1)

            num_less_mid = count_pairs_less_than_val(sorted_arr, mid)

            if num_less_mid > self.k:
                high = mid - 1
            elif num_less_mid == self.k:
                return mid
            else:
                low = mid

        return low


