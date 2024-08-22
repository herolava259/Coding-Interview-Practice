from typing import List


class TriangleSolution:
    def __init__(self, triangle: List[List[int]]):

        self.triangle = triangle

    def solve(self) -> int:

        n = len(self.triangle[-1])

        h_tria = len(self.triangle)
        dp = [self.triangle[0][0]]

        for d in range(1, h_tria):
            len_row = d + 1
            tmp_dp = []

            for i in range(len_row):
                if i == len_row - 1:
                    tmp_dp.append(dp[i - 1] + self.triangle[d][i])
                    continue
                if i == 0:
                    tmp_dp.append(dp[i] + self.triangle[d][i])
                    continue

                tmp_dp.append(min(dp[i - 1], dp[i]) + self.triangle[d][i])

            dp = tmp_dp

        return min(dp)


triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
sln = TriangleSolution(triangle1)
print(sln.solve())
