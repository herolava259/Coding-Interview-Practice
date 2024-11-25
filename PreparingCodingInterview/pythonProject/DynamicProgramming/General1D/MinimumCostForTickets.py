from typing import List

class MinimumCostForTicketSolution:
    def __init__(self, days: List[int], costs: List[int]):

        self.days: List[int] = days
        self.costs: List[int] = costs

    def naive_solve(self) -> int:

        day_pass_costs = [(1, self.costs[0]), (7, self.costs[1]), (30, self.costs[2])]
        num_buy_days = len(self.days)


        first_day, last_day = self.days[0], self.days[-1]

        dp: List[int] = [1000000000] * (last_day + 1)
        dp[last_day] = min(self.costs)

        for doy in range(last_day-1, first_day-1, -1):
            if doy not in self.days:
                dp[doy] = dp[doy+1]
                continue

            for day_pass, cost in day_pass_costs:
                prev_cost = 0 if doy + day_pass > last_day else dp[doy + day_pass]
                dp[doy] = min(dp[doy], prev_cost + cost)

        return dp[first_day]


days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

sln = MinimumCostForTicketSolution(days, costs)

print(sln.naive_solve())



