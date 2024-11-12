from typing import List


class LongestChainSolution:
    def __init__(self, pairs: List[List[int]]):
        self.pairs: List[List[int]] = pairs

    def solve(self) -> int:
        sorted_pairs = sorted(self.pairs, key=lambda c: c[0])
        dp: List[int] = [1] * len(self.pairs)
        for idx, pair in enumerate(sorted_pairs):

            for i in range(idx):
                if pair[0] > sorted_pairs[i][1]:
                    dp[idx] = max(dp[idx], dp[i] + 1)

        return max(dp)


pairs1 = [[1,2],[7,8],[4,5]]

sln = LongestChainSolution(pairs1)

print(sln.solve())
