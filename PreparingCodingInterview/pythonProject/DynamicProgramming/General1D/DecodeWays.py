from typing import List

class NumOfDecodingSolution:
    def __init__(self, s: str):

        self.s: str = s

    def solve(self) -> int:

        n_s = len(self.s)

        if self.s[0] == '0':
            return 0
        if n_s == 1:
            return 1

        dp: List[int] = [0] * (n_s+1)

        dp[1] = 1
        dp[0] = 1

        for i in range(1, n_s):
            if self.s[i] != '0':
                dp[i + 1] = dp[i]

            if self.s[i-1] == '0' or int(self.s[i-1:i+1]) > 26:
                continue
            dp[i+1] += dp[i-1]

        return dp[n_s]


s = '06'

sln = NumOfDecodingSolution(s)

print(sln.solve())