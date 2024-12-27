from typing import List


class SingleNonDuplicateSolution:
    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> int:

        n: int = len(self.nums)

        low, high = 0, n - 1

        while low < high:

            mid = (low + high) >> 1

            left_val = self.nums[mid - 1] if mid > 0 else -1
            right_val = self.nums[mid + 1] if mid < n - 1 else -1
            cur_val = self.nums[mid]

            total_left, total_right = 0, 0
            left_idx, right_idx = mid - 2, mid
            if left_val == cur_val:
                total_left = mid - 1
                total_right = n - 1 - mid
                left_idx = mid - 2
                right_idx = mid + 1
            elif right_val == cur_val:
                total_left = mid
                total_right = n - 2 - mid
                left_idx = mid - 1
                right_idx = mid + 2
            else:
                return cur_val

            if total_left > 0 and total_left % 2 == 1:
                high = left_idx
            elif total_right > 0 and total_right % 2 == 1:
                low = right_idx
            else:
                break

        if low < 0:
            low = 0
        elif low >= n:
            low = n-1
        return self.nums[low]

nums1: List[int] = [3,3,7,7,10,11,11]

sln = SingleNonDuplicateSolution(nums1)

print(sln.solve())