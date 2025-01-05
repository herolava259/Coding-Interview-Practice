from typing import List


class MinCostClimbingStairs:
    def __init__(self, cost: List[int]):
        self.cost: List[int] = cost

    def solve(self) -> int:
        dp = min(self.cost[0], self.cost[1])

        dp0, dp1 = self.cost[0], self.cost[1]

        for i in range(2, len(self.cost)):
            dp2 = min(dp1, dp0) + self.cost[i]

            dp = min(dp2, dp)

            dp0, dp1 = dp1, dp2

        return dp
