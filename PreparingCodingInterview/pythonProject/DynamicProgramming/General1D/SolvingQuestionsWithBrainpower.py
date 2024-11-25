from typing import List

class MostPointsSolution:
    def __init__(self, questions: List[List[int]]):
        self.questions: List[List[int]] = questions

    def naive_solve(self) -> int:

        n_qs: int = len(self.questions)

        dp: List[int] = [0] * n_qs
        max_dp = 0
        for i in range(n_qs):

            point, _ = self.questions[i]

            for idx in range(i):
                _, skip = self.questions[idx]
                if i - idx <= skip:
                    continue
                dp[i] = max(dp[i], dp[idx])

            dp[i] += point
            max_dp = max(max_dp, dp[i])



        return max_dp

    def solve(self) -> int:

        n_qs: int = len(self.questions)

        dp: List[int] = [0] * n_qs

        last_dp = [0] * n_qs
        max_dp = 0

        for i in range(n_qs):

            point, skip = self.questions[i]

            last_dp[i] = max(last_dp[i], last_dp[i - 1])
            dp[i] = last_dp[i] + point

            max_dp = max(max_dp, dp[i])

            if i + skip + 1 >= n_qs:
                continue
            last_dp[i+skip + 1] = max(last_dp[i+skip + 1], dp[i])


        return max_dp

questions1 = [[1,1],[2,2],[3,3],[4,4],[5,5]]

sln = MostPointsSolution(questions1)

print(sln.solve())

