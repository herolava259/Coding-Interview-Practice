from typing import List


class MinSizeSubSumSolution:
    def __init__(self, target: int, nums: List[int]):
        self.target: int = target
        self.nums: List[int] = nums

    def naive_solve(self) -> int:

        min_len = 100000

        n = len(self.nums)

        for i in range(n):

            cur_idx = i
            sum_arr = 0

            while cur_idx < n and sum_arr < self.target:
                sum_arr += self.nums[cur_idx]
                cur_idx += 1

            if sum_arr < self.target:
                continue

            min_len = min(cur_idx - i, min_len)

        if min_len > n:
            return 0

        return min_len

    def binary_search_solve(self):

        n = len(self.nums)
        prefix_sums = [0 for _ in range(n)]

        prefix_sums[0] = self.nums[0]

        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + self.nums[i]

        if prefix_sums[0] > self.target:
            return 1
        min_len = 1000000

        for i in range(1, n):

            target = self.target + prefix_sums[i - 1]

            end_idx = binary_search(prefix_sums, i, n - 1, target)

            if end_idx != -1:
                min_len = min(min_len, end_idx - i + 1)

        if min_len > n:
            return 0
        return min_len

    def dp_solve(self) -> int:

        dp_sum = self.nums[0]
        dp_first_idx = 0
        dp_min_len = 1000000

        if self.nums[0] >= self.target:
            return 1
        n = len(self.nums)
        for i in range(1, n):
            if dp_sum + self.nums[i] < self.target:
                dp_sum += self.nums[i]
                continue
            if self.nums[dp_first_idx] >= self.nums[i]:
                cd_sum = dp_sum - self.nums[dp_first_idx] + self.nums[i]
                if cd_sum >= self.target:
                    dp_sum = cd_sum
                    dp_first_idx += 1
                else:
                    dp_sum += self.nums[i]
                dp_min_len = min(dp_min_len, i-dp_first_idx+1)
                continue
            dp_sum += self.nums[i]
            while dp_first_idx <= i and dp_sum - self.nums[dp_first_idx] >= self.target:
                dp_sum -= self.nums[dp_first_idx]
                dp_first_idx += 1
            dp_min_len = min(dp_min_len, i - dp_first_idx + 1)

        if dp_min_len > n:
            return 0
        return dp_min_len


def binary_search(arr, first: int, last: int, target: int) -> int:
    while first < last:
        mid = (first + last) // 2

        if arr[mid] >= target:
            last = mid
        else:
            first = mid + 1

    if arr[first] < target:
        return -1
    return first


tar_1 = 7
nums1 = [2, 3, 1, 2, 4, 3]

sln = MinSizeSubSumSolution(tar_1, nums1)

print(sln.dp_solve())
