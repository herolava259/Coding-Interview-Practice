from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canReach = [0 for _ in nums]
        canReach[-1] = nums[-1]
        n = len(nums)
        for i in range(n - 2, -1, -1):
            limit = min(nums[i], n - 1 - i)
            canReach[i] = nums[i]
            for k in range(limit+1):
                canReach[i] = max(canReach[i + k] + k, canReach[i])

        return canReach[0] >= n - 1


sln = Solution()

nums1 = [1,2,3]
print(sln.canJump(nums1))