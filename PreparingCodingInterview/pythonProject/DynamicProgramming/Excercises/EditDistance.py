
class EditDistanceSolution:
    def __init__(self, word1: str, word2: str):
        self.word1: str = word1
        self.word2: str = word2

    def solve(self) -> int:
        dp = [[100000000] * (len(self.word2) + 1) for _ in range(len(self.word1) + 1)]
        dp[0][0] = 0
        for i in range(1, len(self.word2) + 1):
            dp[0][i] = i

        for i in range(1, len(self.word1) + 1):
            dp[i][0] = i

        for i in range(1, len(self.word1) + 1):
            for j in range(1, len(self.word2) + 1):

                if self.word1[i-1] == self.word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]

                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[len(self.word1)][len(self.word2)]


word11 = 'intention'
word12 = 'execution'

sln = EditDistanceSolution(word11, word12)

print(sln.solve())
