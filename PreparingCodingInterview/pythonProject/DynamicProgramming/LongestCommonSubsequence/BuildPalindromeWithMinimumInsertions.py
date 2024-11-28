from typing import List

class MinInsertionSolution:
    def __init__(self, s: str):

        self.s: str = s

    def solve(self) -> int:
        n = len(self.s)

        dp: List[List[int]] = [[1 if i <= j else 0 for j in range(n)] for i in range(n)]

        for len_sq in range(2, n+1):
            for i in range(n-len_sq+1):
                first, last = i, i+ len_sq-1
                dp[first][last] = max(dp[first][last-1], dp[first+1][last])
                if self.s[first] == self.s[last]:
                    dp[first][last] = max(dp[first][last], dp[first+1][last-1] + 2)

        return n - dp[0][-1]

s = "zjveiiwvc"

sln = MinInsertionSolution(s)

print(sln.solve())