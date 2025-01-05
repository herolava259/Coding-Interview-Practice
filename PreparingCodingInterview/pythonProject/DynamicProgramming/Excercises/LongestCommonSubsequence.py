from typing import List


class LongestCommonSubsequence:

    def __init__(self, txt1: str, txt2: str):
        self.txt1: str = txt1
        self.txt2: str = txt2

    def solve(self) -> int:

        len_txt1 = len(self.txt1)
        len_txt2 = len(self.txt2)

        dp: List[List[int]] = [[0] * (len_txt2 + 1) for _ in range(len_txt1 + 1)]

        for i in range(1, len_txt1 + 1):
            for j in range(1, len_txt2 + 1):

                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

                c1, c2 = self.txt1[i - 1], self.txt2[j - 1]

                if c1 == c2:
                    dp[i][j] = max(dp[i][j], 1 + dp[i - 1][j - 1])

        return dp[-1][-1]


txt11 = "abc"
txt21 = 'abc'
sln = LongestCommonSubsequence(txt11, txt21)

print(sln.solve())

