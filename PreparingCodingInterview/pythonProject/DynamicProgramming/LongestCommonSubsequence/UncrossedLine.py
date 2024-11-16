from typing import List


class UncrossedLineSolution:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2

    def solve(self) -> int:
        n1, n2 = len(self.nums1), len(self.nums2)

        dp = [[0] * (n2+1) for _ in range(n1+1)]

        max_cl = 0

        for i in range(1, n1+1):
            for j in range(1, n2+1):

                dp[i][j] = max(dp[i][j-1], dp[i-1][j])

                if self.nums1[i - 1] == self.nums2[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                max_cl = max(max_cl, dp[i][j])

        return max_cl



nums11 = [1,3,7,1,7,5]
nums21 = [1,9,2,5,1]

sln = UncrossedLineSolution(nums11, nums21)

print(sln.solve())
