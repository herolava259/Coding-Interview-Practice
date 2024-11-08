from typing import List


class LongestPalindromeSubsequenceSolution:
    def __init__(self, s: str):
        self.s: str = s

    def solve(self) -> int:

        n = len(self.s)

        dp: List[List[int]] = [[1 for j in range(n)] for i in range(n)]

        max_len = 0

        for offset in range(2, n+1):
            for i in range(n):
                j = i + offset - 1
                if j >= n:
                    continue
                if self.s[i] == self.s[j]:
                    if offset == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = max(2+dp[i+1][j-1], dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                max_len = max(dp[i][j], max_len)

        return max_len


s = 'cbd'

sln = LongestPalindromeSubsequenceSolution(s)

print(sln.solve())
