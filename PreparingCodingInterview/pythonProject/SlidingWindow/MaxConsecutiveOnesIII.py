from typing import List, Deque
from collections import deque

'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
'''


class MaxConsecutiveOnesIIISolution:
    def __init__(self, nums: List[int], k: int):
        self.nums: List[int] = nums
        self.k: int = k

    def solve(self) -> int:
        if self.k == 0:
            return self.special_solve()
        q: Deque[int] = deque()
        remain_k = self.k
        max_seq = 0
        first_idx = 0
        for idx, item in enumerate(self.nums):
            # max_seq = max(max_seq, idx - q[0])
            if item == 1:
                continue
            if remain_k > 0:
                remain_k -= 1
                q.append(idx)
            else:
                max_seq = max(max_seq, idx - first_idx)
                first_idx = q.popleft() + 1
                q.append(idx)
        max_seq = max(max_seq, len(self.nums) - first_idx)

        return max_seq

    def special_solve(self) -> int:

        first_idx, last_idx = 0, -1
        max_seq = 0
        for i in range(len(self.nums)):
            if self.nums[i] == 1:
                if i > 0 and self.nums[i - 1] == 0:
                    first_idx = i
                last_idx = i
            else:
                max_seq = max(last_idx - first_idx + 1, max_seq)

        max_seq = max(max_seq, last_idx - first_idx + 1)
        return max_seq

    def dp_solve(self) -> int:

        if self.k == 0:
            return self.special_solve()

        before_ones: List[int] = []

        first_idx = -1

        for idx, item in enumerate(self.nums):
            if item == 0:
                before_ones.append(idx - first_idx)
                first_idx = idx
        if len(before_ones) == 0:
            return len(self.nums)

        before_ones.append(len(self.nums) - first_idx - 1)

        remain_k = self.k + 1

        max_seq = 0
        cur_seq = 0

        for idx, num_one in enumerate(before_ones):
            if remain_k > 0:
                remain_k -= 1
                cur_seq += num_one
            else:
                max_seq = max(max_seq, cur_seq-1)
                cur_seq += num_one - before_ones[idx - self.k-1]

        return max(cur_seq, max_seq)


nums1 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k1 = 3

sln = MaxConsecutiveOnesIIISolution(nums1, k1)

print(sln.dp_solve())
