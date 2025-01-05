from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, cur_sum = -1000000009, -1000000009
        n = len(nums)

        cum_sums = []
        cum_sum = 0
        for e in nums:
            cum_sum += e
            cum_sums.append(cum_sum)
            tmp_sum = cur_sum + e

            if tmp_sum <= e:
                cur_sum = e
            else:
                cur_sum = tmp_sum

            if max_sum < cur_sum:
                max_sum = cur_sum
        last_sum = -1000000009
        tmp_sum = 0
        for idx in range(n - 1, 0, -1):
            tmp_sum += nums[idx]
            last_sum = max(tmp_sum, last_sum)

            max_sum = max(last_sum + cum_sums[idx - 1], max_sum)

        return max_sum

sln = Solution()

nums1 = [-3,-2,-3]

print(sln.maxSubarraySumCircular(nums1))
